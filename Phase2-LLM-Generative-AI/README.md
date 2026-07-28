# Giai đoạn 2 — LLM và Generative AI

## Project

| Project | Kỹ năng chính |
|---|---|
| [01 PDF Chatbot](./01-pdf-chatbot/README.md) | File input, multi-turn context, hallucination boundary |
| [02 Document Summarizer](./02-document-summarizer/README.md) | Prompting, streaming, output length |
| [03 Structured JSON Extractor](./03-structured-json-extractor/README.md) | Pydantic, structured output, schema validation |
| [04 Tool Calling CLI](./04-tool-calling-cli/README.md) | Function calling, validation, allowlist, bounded loop |

Thực hiện theo thứ tự. Mỗi project tạo virtual environment riêng.

## Cổng hoàn thành

- Phân biệt được `instructions` và user input.
- Output dùng cho máy phải qua schema, không parse JSON tự do bằng regex.
- Tool chỉ được gọi qua allowlist và input phải validate.
- Streaming UI xử lý được event delta và lỗi giữa luồng.
- Biết model, context và prompt đều phải cấu hình/đánh giá thay vì hard-code khắp codebase.
