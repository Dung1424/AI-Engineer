# Project 02 — Document Summarizer

## Mục tiêu

Tóm tắt file text/Markdown theo ba kiểu và hiển thị kết quả dạng streaming. Project minh họa instruction rõ, điều khiển output và xử lý stream event.

## Chạy

```bash
cd Phase2-LLM-Generative-AI/02-document-summarizer
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python summarize.py sample.txt --style actions
```

`--style` nhận `brief`, `detailed` hoặc `actions`.

## Đánh giá

Tạo 10 tài liệu mẫu và kiểm tra: giữ đúng tên/số liệu, không thêm dữ kiện, không bỏ action quan trọng, đúng format. So sánh ít nhất hai prompt trên cùng test set.

## Tài liệu chính thức

- [Streaming Responses](https://developers.openai.com/api/docs/guides/streaming-responses)
- [Prompt engineering](https://developers.openai.com/api/docs/guides/prompt-engineering)
