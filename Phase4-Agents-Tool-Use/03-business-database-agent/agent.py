import argparse
import json
import os
import re
import sqlite3
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel, Field

DB = Path("business.db")


class QueryInput(BaseModel):
    sql: str = Field(min_length=8, max_length=1000)


TOOLS = [{
    "type": "function",
    "name": "run_readonly_query",
    "description": "Chạy một SELECT read-only trên sales(order_id, region, product, quantity, revenue, ordered_at). Tối đa 100 dòng.",
    "parameters": QueryInput.model_json_schema(),
    "strict": True,
}]


def seed() -> None:
    with sqlite3.connect(DB) as db:
        db.execute("CREATE TABLE IF NOT EXISTS sales(order_id INTEGER PRIMARY KEY, region TEXT, product TEXT, quantity INTEGER, revenue REAL, ordered_at TEXT)")
        if db.execute("SELECT COUNT(*) FROM sales").fetchone()[0] == 0:
            db.executemany("INSERT INTO sales VALUES(?,?,?,?,?,?)", [
                (1, "north", "RAG Course", 2, 198.0, "2026-06-02"),
                (2, "south", "Agent Course", 1, 129.0, "2026-06-05"),
                (3, "north", "Agent Course", 3, 387.0, "2026-07-01"),
                (4, "west", "LLM Handbook", 5, 245.0, "2026-07-10"),
            ])


def query(raw: dict[str, Any]) -> dict[str, Any]:
    sql = QueryInput.model_validate(raw).sql.strip()
    if not re.match(r"(?is)^select\b", sql) or ";" in sql or re.search(r"(?i)\b(insert|update|delete|drop|alter|attach|pragma)\b", sql):
        raise ValueError("Chỉ cho phép một câu SELECT")
    with sqlite3.connect(f"file:{DB}?mode=ro", uri=True) as db:
        db.row_factory = sqlite3.Row
        rows = [dict(row) for row in db.execute(f"SELECT * FROM ({sql}) LIMIT 100").fetchall()]
    return {"rows": rows, "count": len(rows)}


def run(question: str) -> str:
    seed()
    client = OpenAI()
    items: list[Any] = [{"role": "user", "content": question}]
    for _ in range(4):
        response = client.responses.create(
            model=os.getenv("OPENAI_MODEL", "gpt-5.6-luna"),
            instructions="Dùng tool để trả lời bằng số liệu. Không đoán dữ liệu. SQL phải tương thích SQLite.",
            tools=TOOLS,
            input=items,
        )
        items.extend(response.output)
        calls = [item for item in response.output if item.type == "function_call"]
        if not calls:
            return response.output_text
        for call in calls:
            try:
                result = {"ok": True, "data": query(json.loads(call.arguments))}
            except (ValueError, sqlite3.Error) as exc:
                result = {"ok": False, "error": str(exc)}
            items.append({"type": "function_call_output", "call_id": call.call_id, "output": json.dumps(result)})
    raise RuntimeError("Vượt giới hạn tool loop")


if __name__ == "__main__":
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument("question")
    print(run(parser.parse_args().question))
