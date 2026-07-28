# Project 02 — Multi-source Q&A

## Mục tiêu

Nạp dữ liệu từ PDF, website và file Markdown export từ Notion. Mỗi chunk giữ `source_type`, cho phép filter retrieval theo nguồn.

## Chạy

```bash
cd Phase3-RAG/02-multi-source-qa
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python multisource.py ingest handbook.pdf notion-export/page.md https://example.com/docs
python multisource.py ask "Quy trình onboarding?" --type notion_export
```

Chỉ tải website bạn được phép truy cập; tôn trọng robots.txt, điều khoản và dữ liệu cá nhân. Notion được dùng ở dạng export để project không phụ thuộc tài khoản thật.

## Bài tập

Thêm sitemap loader, retry HTTP, page metadata cho PDF, dedup giữa website/Notion và filter theo ngày cập nhật.
