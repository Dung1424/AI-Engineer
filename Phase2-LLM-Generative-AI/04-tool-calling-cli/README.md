# Project 04 — Tool Calling CLI

## Mục tiêu

Cho model chọn giữa calculator và product lookup, nhưng code mới là nơi validate và thực thi. Agent có allowlist hai tool và dừng sau tối đa năm vòng.

## Chạy

```bash
cd Phase2-LLM-Generative-AI/04-tool-calling-cli
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python agent.py "Hai bộ RAG-01 cộng thêm phí 3.5 thì tổng bao nhiêu?"
```

## Điểm cần đọc trong code

- Pydantic validate arguments trước khi gọi hàm.
- `HANDLERS` là allowlist; model không thể gọi hàm tùy ý.
- Tool output luôn trả JSON có `ok` hoặc lỗi rõ ràng.
- Vòng lặp có giới hạn, tránh model gọi tool vô hạn.

## Bài tập

Thêm timeout, log từng tool call và test cho chia 0, SKU lạ, tool name lạ, arguments sai schema.

## Tài liệu chính thức

- [Function calling](https://developers.openai.com/api/docs/guides/function-calling)
