# Project 03 — Embedding Semantic Search

## Mục tiêu

Biến query/document thành vector chuẩn hóa và dùng dot product như cosine similarity. Project chạy local bằng model multilingual từ Hugging Face.

## Chạy

```bash
cd Phase1-AI-ML-Foundation/03-embedding-semantic-search
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python search.py "làm sao tìm tài liệu theo ý nghĩa" --top-k 3
```

## Phải giải thích được

- Vì sao vector đã normalize thì dot product bằng cosine similarity.
- Semantic search khác keyword search ở đâu.
- Tại sao score cao không tự động có nghĩa kết quả đúng.

Tạo 20 query có expected document, tính Recall@1 và Recall@3, rồi thêm các truy vấn khó/không liên quan để phân tích lỗi.
