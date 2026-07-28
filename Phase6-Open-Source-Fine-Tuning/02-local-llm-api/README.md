# Project 02 — Local LLM API

FastAPI wrapper chạy **local** trên Ollama; không có Docker/cloud deployment.

```bash
ollama pull qwen3:4b
ollama serve

cd Phase6-Open-Source-Fine-Tuning/02-local-llm-api
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
OLLAMA_MODEL=qwen3:4b uvicorn app:app --reload
curl -X POST http://127.0.0.1:8000/chat -H 'content-type: application/json' -d '{"message":"Giải thích quantization"}'
```

Ghi RAM/VRAM, time-to-first-token, total latency và tokens/second cho từng quantization/model. Kiểm tra model license trước khi phân phối.
