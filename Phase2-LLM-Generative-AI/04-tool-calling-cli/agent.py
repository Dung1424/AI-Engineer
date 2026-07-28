from __future__ import annotations

import argparse
import json
import operator
import os
from typing import Any, Callable

from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel, Field


class CalculatorInput(BaseModel):
    left: float
    operator: str = Field(pattern=r"^[+\-*/]$")
    right: float


class ProductInput(BaseModel):
    sku: str = Field(min_length=2, max_length=20)


PRODUCTS = {
    "AI-101": {"name": "AI Engineer Handbook", "price": 29.0, "stock": 12},
    "RAG-01": {"name": "RAG Practice Dataset", "price": 15.0, "stock": 5},
}


def calculate(raw: dict[str, Any]) -> dict[str, float]:
    data = CalculatorInput.model_validate(raw)
    operations: dict[str, Callable[[float, float], float]] = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }
    if data.operator == "/" and data.right == 0:
        raise ValueError("Không thể chia cho 0")
    return {"result": operations[data.operator](data.left, data.right)}


def lookup_product(raw: dict[str, Any]) -> dict[str, Any]:
    data = ProductInput.model_validate(raw)
    return PRODUCTS.get(data.sku.upper(), {"error": "SKU không tồn tại"})


TOOLS = [
    {
        "type": "function",
        "name": "calculate",
        "description": "Tính một phép toán số học đơn giản.",
        "parameters": CalculatorInput.model_json_schema(),
        "strict": True,
    },
    {
        "type": "function",
        "name": "lookup_product",
        "description": "Tra cứu tên, giá và tồn kho theo SKU.",
        "parameters": ProductInput.model_json_schema(),
        "strict": True,
    },
]
HANDLERS = {"calculate": calculate, "lookup_product": lookup_product}


def run(query: str) -> str:
    load_dotenv()
    client = OpenAI()
    model = os.getenv("OPENAI_MODEL", "gpt-5.6-luna")
    items: list[Any] = [{"role": "user", "content": query}]

    for _ in range(5):
        response = client.responses.create(
            model=model,
            instructions="Dùng tool khi cần. Không tự bịa kết quả tool.",
            tools=TOOLS,
            input=items,
        )
        items.extend(response.output)
        calls = [item for item in response.output if item.type == "function_call"]
        if not calls:
            return response.output_text

        for call in calls:
            try:
                handler = HANDLERS[call.name]
                output = handler(json.loads(call.arguments))
                result = {"ok": True, "data": output}
            except (KeyError, TypeError, ValueError) as exc:
                result = {"ok": False, "error": str(exc)}
            items.append(
                {
                    "type": "function_call_output",
                    "call_id": call.call_id,
                    "output": json.dumps(result, ensure_ascii=False),
                }
            )
    raise RuntimeError("Agent vượt quá giới hạn 5 vòng tool")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("query")
    print(run(parser.parse_args().query))
