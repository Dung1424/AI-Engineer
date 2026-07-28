import argparse
import os
from datetime import date

from dotenv import load_dotenv
from openai import OpenAI


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("question")
    args = parser.parse_args()
    load_dotenv()
    response = OpenAI().responses.create(
        model=os.getenv("OPENAI_MODEL", "gpt-5.6-luna"),
        instructions=(
            f"Hôm nay là {date.today().isoformat()}. Nghiên cứu câu hỏi bằng web search. "
            "Ưu tiên nguồn gốc/official, phân biệt fact và inference, cuối bài có danh sách nguồn."
        ),
        tools=[{"type": "web_search"}],
        input=args.question,
    )
    print(response.output_text)


if __name__ == "__main__":
    main()
