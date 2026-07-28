# Project 03 — Personal Document Search

## Mục tiêu

Xây semantic search chạy local: Sentence Transformers tạo embedding, NumPy tính cosine similarity. Không dùng LLM API và không sinh câu trả lời, nên bạn quan sát retrieval trực tiếp.

## Chạy

```bash
cd Phase3-RAG/03-personal-document-search
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python search.py build documents
python search.py search "ghi chú về vector database" --top-k 5
```

Lần đầu model được tải từ Hugging Face. `vectors.npy` và `records.json` là index local, có thể xóa và build lại.

## Bài tập

So sánh semantic search với BM25/keyword, thêm metadata filter và đo Recall@5 trên 30 truy vấn tự gán nhãn.
