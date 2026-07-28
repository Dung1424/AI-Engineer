# Danh mục project AI Engineer

Phạm vi triển khai đã chốt:

- Bỏ qua Giai đoạn 0 — nền tảng lập trình.
- Triển khai Giai đoạn 1 — nền tảng AI/ML.
- Triển khai Giai đoạn 2 — LLM và Generative AI.
- Triển khai Giai đoạn 3 — RAG.
- Triển khai Giai đoạn 4 — Agents và Tool Use.
- Bỏ qua Giai đoạn 5 — LLMOps, production và deployment.
- Triển khai Giai đoạn 6 — Open-source Models và Fine-tuning; chỉ chạy local.

## Cấu trúc

| Giai đoạn | Thư mục | Số project |
|---|---|---:|
| 1 — AI/ML | [`Phase1-AI-ML-Foundation`](./Phase1-AI-ML-Foundation/README.md) | 3 |
| 2 — LLM | [`Phase2-LLM-Generative-AI`](./Phase2-LLM-Generative-AI/README.md) | 4 |
| 3 — RAG | [`Phase3-RAG`](./Phase3-RAG/README.md) | 3 |
| 4 — Agents | [`Phase4-Agents-Tool-Use`](./Phase4-Agents-Tool-Use/README.md) | 4 |
| 6 — Open-source | [`Phase6-Open-Source-Fine-Tuning`](./Phase6-Open-Source-Fine-Tuning/README.md) | 3 |

Mỗi project có dependency, `.env.example`, dữ liệu mẫu và README riêng. Không cài tất cả dependency vào một virtual environment.

Yêu cầu chung: Python 3.11+; khuyến nghị Python 3.12. Các project dùng API cần tự điền `OPENAI_API_KEY` vào `.env` của chính project.

## Quy ước hoàn thành

Một project chỉ hoàn thành khi:

1. Cài và chạy được theo đúng README.
2. Không chứa API key hoặc dữ liệu riêng tư trong Git.
3. Có input mẫu, output mong đợi và cách xử lý lỗi.
4. Có phần giải thích kiến trúc, giới hạn và bài tập mở rộng.
5. Các đoạn không cần model thật có test tự động.
