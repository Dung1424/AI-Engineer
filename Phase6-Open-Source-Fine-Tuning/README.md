# Giai đoạn 6 — Open-source Models và Fine-tuning

| Project | Trọng tâm |
|---|---|
| [01 Intent Fine-tuning](./01-intent-finetuning/README.md) | Transformers, Datasets, Trainer, evaluation |
| [02 Local LLM API](./02-local-llm-api/README.md) | Ollama local, streaming, model config |
| [03 API vs Local Benchmark](./03-api-vs-local-benchmark/README.md) | So sánh quality/latency giữa API và local |

Không deploy cloud/production. Model và dataset phải kiểm tra license trước khi dùng ngoài mục đích học tập.

## Cổng hoàn thành

- Có baseline trước fine-tune và holdout test sau fine-tune.
- Không train/test trên dữ liệu trùng nhau.
- Ghi model ID, dataset version, seed, hyperparameters và phần cứng.
- Fine-tune chỉ được coi là có ích khi metric holdout tăng đủ để bù chi phí vận hành.
