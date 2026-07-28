# Giai đoạn 3 — Retrieval-Augmented Generation

| Project | Mục đích |
|---|---|
| [01 Knowledge Bot](./01-company-knowledge-bot/README.md) | Pipeline PDF/text → chunk → embed → Chroma → citation |
| [02 Multi-source QA](./02-multi-source-qa/README.md) | Nạp PDF, website và Notion export với metadata filter |
| [03 Personal Search](./03-personal-document-search/README.md) | Semantic search local, không cần LLM API |

## Cổng hoàn thành

- Chạy ingestion nhiều lần không nhân bản chunk.
- Mỗi chunk giữ `source`, page và chunk index.
- Tách riêng retrieval quality khỏi answer quality.
- Câu không có evidence phải trả “không tìm thấy”.
- Có bộ câu hỏi kiểm tra gồm câu đúng, câu ngoài phạm vi và câu dễ nhầm.
