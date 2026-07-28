# Project 01 — Company Knowledge Bot

## Mục tiêu

Tự xây pipeline RAG cơ bản với PDF/TXT/Markdown, Chroma local, embeddings API và citation. ID của chunk được hash từ source/page/content nên chạy ingestion lại không tạo duplicate.

## Chạy

```bash
cd Phase3-RAG/01-company-knowledge-bot
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
mkdir -p documents
python rag.py ingest documents
python rag.py ask "Chính sách nghỉ phép là gì?"
```

## Thí nghiệm

Thử `size/overlap`, `top-k` và ghi Recall@k trên ít nhất 30 câu hỏi. Kiểm tra citation thủ công trước khi đánh giá văn phong câu trả lời.

## Giới hạn

Chưa có OCR, hybrid search hay reranker. Đây là baseline để so sánh ở các lần nâng cấp.
