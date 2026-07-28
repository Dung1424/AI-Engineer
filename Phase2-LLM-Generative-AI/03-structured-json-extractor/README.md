# Project 03 — Structured JSON Extractor

## Mục tiêu

Chuyển biên bản tự nhiên thành JSON đúng Pydantic schema. Structured Outputs giúp output bám JSON Schema; vẫn cần quy tắc nghiệp vụ để tránh model tự suy đoán dữ liệu thiếu.

## Chạy

```bash
cd Phase2-LLM-Generative-AI/03-structured-json-extractor
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python extract.py sample-meeting.txt
```

## Bài tập

Thêm `risks`, enum trạng thái action và validation deadline không trước ngày họp. Tạo 20 input gồm ngày mơ hồ, thiếu owner và nội dung không phải biên bản.

## Tài liệu chính thức

- [Structured model outputs](https://developers.openai.com/api/docs/guides/structured-outputs)
