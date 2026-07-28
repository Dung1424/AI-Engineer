# Project 01 — PDF Chatbot

## Mục tiêu

Upload một PDF lên API, hỏi đáp nhiều lượt và buộc chatbot thừa nhận khi tài liệu không chứa câu trả lời. Đây là bước làm quen với document input; RAG tự xây nằm ở Giai đoạn 3.

## Chạy

```bash
cd Phase2-LLM-Generative-AI/01-pdf-chatbot
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# điền OPENAI_API_KEY trong .env
python chat.py path/to/document.pdf
```

File đã upload được xóa khi thoát. Dùng `--keep-file` nếu muốn giữ lại để kiểm tra thủ công.

## Luồng

```text
PDF → Files API → Responses API + file_id → response.id → previous_response_id
```

## Thử nghiệm bắt buộc

1. Hỏi câu có đáp án trực tiếp trong PDF.
2. Hỏi câu cần tổng hợp hai đoạn.
3. Hỏi một thông tin chắc chắn không có trong PDF.
4. Ghi latency và chất lượng vào `experiments.md`.

## Tài liệu chính thức

- [OpenAI developer quickstart](https://developers.openai.com/api/docs/quickstart)
- [File inputs](https://developers.openai.com/api/docs/guides/pdf-files)
