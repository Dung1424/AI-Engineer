from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI


def main() -> None:
    parser = argparse.ArgumentParser(description="Tóm tắt text/Markdown bằng streaming")
    parser.add_argument("document", type=Path)
    parser.add_argument("--style", choices=["brief", "detailed", "actions"], default="brief")
    args = parser.parse_args()
    if not args.document.is_file():
        raise SystemExit("File không tồn tại.")

    text = args.document.read_text(encoding="utf-8")
    if not text.strip():
        raise SystemExit("File rỗng.")

    load_dotenv()
    client = OpenAI()
    style_rules = {
        "brief": "Tóm tắt tối đa 7 bullet, ưu tiên ý chính.",
        "detailed": "Tóm tắt theo các heading, giữ số liệu và caveat quan trọng.",
        "actions": "Chỉ ra quyết định, người phụ trách, deadline và action items.",
    }
    stream = client.responses.create(
        model=os.getenv("OPENAI_MODEL", "gpt-5.6-luna"),
        instructions=(
            "Bạn là công cụ tóm tắt tài liệu. Không thêm dữ kiện ngoài văn bản. "
            + style_rules[args.style]
        ),
        input=text,
        stream=True,
    )
    for event in stream:
        if event.type == "response.output_text.delta":
            sys.stdout.write(event.delta)
            sys.stdout.flush()
    print()


if __name__ == "__main__":
    main()
