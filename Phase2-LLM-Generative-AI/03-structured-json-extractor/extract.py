from __future__ import annotations

import argparse
import os
from datetime import date
from pathlib import Path
from typing import Literal

from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel, Field


class ActionItem(BaseModel):
    task: str
    owner: str | None = None
    due_date: date | None = None
    priority: Literal["low", "medium", "high"] = "medium"


class MeetingExtraction(BaseModel):
    title: str
    participants: list[str] = Field(default_factory=list)
    decisions: list[str] = Field(default_factory=list)
    action_items: list[ActionItem] = Field(default_factory=list)
    open_questions: list[str] = Field(default_factory=list)


def main() -> None:
    parser = argparse.ArgumentParser(description="Trích xuất biên bản thành JSON có schema")
    parser.add_argument("document", type=Path)
    args = parser.parse_args()
    text = args.document.read_text(encoding="utf-8")

    load_dotenv()
    response = OpenAI().responses.parse(
        model=os.getenv("OPENAI_MODEL", "gpt-5.6-luna"),
        input=[
            {
                "role": "system",
                "content": (
                    "Trích xuất dữ liệu cuộc họp. Không suy đoán owner/deadline; "
                    "dùng null khi văn bản không nêu."
                ),
            },
            {"role": "user", "content": text},
        ],
        text_format=MeetingExtraction,
    )
    if response.output_parsed is None:
        raise SystemExit("Model không trả về dữ liệu có thể parse.")
    print(response.output_parsed.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
