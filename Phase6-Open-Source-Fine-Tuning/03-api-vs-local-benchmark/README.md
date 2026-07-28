# Project 03 — API vs Local Benchmark

Chạy cùng prompt trên OpenAI API và Ollama, ghi output/latency vào `results.json`, sau đó chấm human score trên cùng rubric.

```bash
cd Phase6-Open-Source-Fine-Tuning/03-api-vs-local-benchmark
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt && cp .env.example .env
python benchmark.py
```

So sánh quality, instruction following, JSON validity, latency, privacy, RAM/VRAM và chi phí vận hành. Chạy warm-up trước benchmark chính và lặp mỗi prompt nhiều lần khi cần số liệu ổn định.
