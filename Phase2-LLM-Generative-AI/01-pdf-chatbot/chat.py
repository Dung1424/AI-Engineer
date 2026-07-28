from __future__ import annotations

import argparse
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Chat với một file PDF")
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--keep-file", action="store_true")
    return parser.parse_args()


def main() -> None:
    load_dotenv()
    args = parse_args()
    if not args.pdf.is_file() or args.pdf.suffix.lower() != ".pdf":
        raise SystemExit("Hãy cung cấp một file PDF hợp lệ.")

    client = OpenAI()
    model = os.getenv("OPENAI_MODEL", "gpt-5.6-luna")
    with args.pdf.open("rb") as document:
        uploaded = client.files.create(file=document, purpose="user_data")

    previous_response_id: str | None = None
    first_turn = True
    print("Nhập câu hỏi; dùng /exit để thoát.")
    try:
        while True:
            question = input("Bạn> ").strip()
            if question in {"/exit", "/quit"}:
                break
            if not question:
                continue

            if first_turn:
                user_input: object = [
                    {
                        "role": "user",
                        "content": [
                            {"type": "input_file", "file_id": uploaded.id},
                            {"type": "input_text", "text": question},
                        ],
                    }
                ]
            else:
                user_input = question

            response = client.responses.create(
                model=model,
                instructions=(
                    "Chỉ trả lời dựa trên PDF được cung cấp. "
                    "Nếu tài liệu không có thông tin, nói rõ là không tìm thấy."
                ),
                input=user_input,
                previous_response_id=previous_response_id,
            )
            print(f"AI> {response.output_text}\n")
            previous_response_id = response.id
            first_turn = False
    finally:
        if not args.keep_file:
            client.files.delete(uploaded.id)


if __name__ == "__main__":
    main()
