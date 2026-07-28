import argparse
import json
import os
from pathlib import Path
from typing import Literal

from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel


class TriageResult(BaseModel):
    category: Literal["support", "sales", "billing", "spam", "other"]
    priority: Literal["low", "medium", "high", "urgent"]
    summary: str
    requested_actions: list[str]
    draft_reply: str
    needs_human_review: bool


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("email", type=Path, help="JSON chứa from, subject, body")
    args = parser.parse_args()
    email = json.loads(args.email.read_text(encoding="utf-8"))
    load_dotenv()
    response = OpenAI().responses.parse(
        model=os.getenv("OPENAI_MODEL", "gpt-5.6-luna"),
        instructions=(
            "Phân loại email và tạo bản nháp lịch sự. Không tuyên bố đã hoàn tiền, "
            "hủy đơn hoặc thực hiện hành động. Billing/urgent luôn cần human review."
        ),
        input=json.dumps(email, ensure_ascii=False),
        text_format=TriageResult,
    )
    if response.output_parsed is None:
        raise SystemExit("Không parse được kết quả")
    print(response.output_parsed.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
