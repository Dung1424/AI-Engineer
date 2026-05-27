# AI Engineer Roadmap

> **AI Engineer** = Software Engineer biết xây sản phẩm dùng AI/LLM.
>
> Không nhất thiết phải là nhà nghiên cứu ML, nhưng phải biết **Python**, **backend**, **API**, **dữ liệu**, **LLM**, **RAG**, **agents**, **evaluation**, **deployment** và **bảo mật**.

Dưới đây là lộ trình chi tiết theo thứ tự học.

---

## Giai đoạn 0: Nền tảng lập trình

**Thời gian:** 1–2 tháng (nếu mới bắt đầu)

### Bạn cần học

**Python cơ bản đến khá**

- Biến, hàm, class, module
- List / dict / set, comprehension
- File I/O, JSON, CSV
- Async cơ bản
- Type hints

**Git và command line**

- `git clone`, `commit`, `branch`, `pull`, `push`
- Terminal cơ bản
- Quản lý môi trường bằng venv, pip, uv hoặc conda

**Backend căn bản**

- HTTP, REST API
- FastAPI
- Authentication cơ bản
- Database: PostgreSQL hoặc SQLite
- Docker cơ bản

### Project nên làm

- Todo API bằng FastAPI + SQLite/PostgreSQL
- Web app nhỏ gọi API backend
- Script đọc file CSV, xử lý dữ liệu, xuất báo cáo

---

## Giai đoạn 1: Nền tảng AI/ML

**Thời gian:** 1.5–3 tháng

Bạn không cần học quá sâu toán như researcher, nhưng cần hiểu đủ để không dùng AI như "hộp đen".

### Cần học

**Toán vừa đủ**

- Linear algebra: vector, matrix, dot product, cosine similarity
- Probability: distribution, conditional probability
- Statistics: mean, variance, correlation, sampling
- Calculus cơ bản: gradient là gì

**Machine Learning căn bản**

- Supervised vs unsupervised learning
- Train / validation / test split
- Overfitting, underfitting
- Regression, classification
- Metrics: accuracy, precision, recall, F1, ROC-AUC
- Feature engineering

**Deep Learning căn bản**

- Neural network
- Embedding
- Transformer là gì
- Attention hoạt động ở mức khái niệm

### Project nên làm

- Dự đoán giá nhà bằng scikit-learn
- Phân loại sentiment review
- Tìm kiếm văn bản bằng embedding + cosine similarity

---

## Giai đoạn 2: LLM và Generative AI

**Thời gian:** 1–2 tháng

Đây là phần **quan trọng nhất** cho AI Engineer hiện nay.

### Cần học

**Cách dùng LLM API**

- Prompting
- System / user / developer message
- Structured output JSON
- Function calling / tools
- Streaming response
- Token, context window, cost, latency

**Nguồn nên học**

- [OpenAI API Quickstart](https://platform.openai.com/docs/quickstart)
- [OpenAI Help Center: start exploring the API](https://help.openai.com/)

**Prompt engineering thực dụng**

- Viết instruction rõ
- Few-shot examples
- Output schema
- Guardrails
- Cách giảm hallucination

**Embeddings và semantic search**

- Text embedding
- Vector database
- Similarity search
- Chunking tài liệu
- Metadata filtering

### Project nên làm

- Chatbot trả lời theo tài liệu PDF
- Tool tóm tắt email / tài liệu
- App sinh JSON theo schema từ văn bản tự nhiên

---

## Giai đoạn 3: RAG — Retrieval Augmented Generation

**Thời gian:** 1–2 tháng

RAG là kỹ năng **bắt buộc** nếu muốn làm AI app thực tế.

### Cần học

**Pipeline RAG**

1. Load document
2. Split / chunk
3. Embed
4. Store vector DB
5. Retrieve
6. Rerank
7. Generate answer with citations

**Vector databases**

| Mục đích | Gợi ý |
|----------|-------|
| Học local | Chroma, FAISS |
| Production | Qdrant, Weaviate, Pinecone, pgvector |

**Các vấn đề thực tế**

- Chunk size bao nhiêu?
- Truy xuất sai tài liệu thì xử lý sao?
- Làm sao có citation?
- Làm sao đánh giá câu trả lời đúng / sai?

### Project nên làm

- Internal company knowledge bot
- Chatbot hỏi đáp trên bộ PDF / Notion / website
- Search engine nhỏ cho tài liệu cá nhân

---

## Giai đoạn 4: Agents và Tool Use

**Thời gian:** 1–2 tháng

Agent không phải lúc nào cũng cần, nhưng đang là kỹ năng rất quan trọng.

### Cần học

**Tool calling**

- LLM gọi function
- Validate input / output
- Retry khi lỗi
- Không cho model tự do chạy tool nguy hiểm

**Agent workflow**

- Plan → Act → Observe → Reflect
- Multi-step task

**Framework**

| Framework | Dùng khi |
|-----------|----------|
| LangGraph | Workflow agent có state |
| LangChain | Dùng vừa đủ, không phụ thuộc mù quáng |
| LlamaIndex | RAG / document apps |
| Hugging Face agents | Muốn học open-source ecosystem |

**Nguồn nên xem**

- [LangGraph official docs](https://langchain-ai.github.io/langgraph/)
- [Hugging Face AI Agents Course](https://huggingface.co/learn/agents-course/)
- [DeepLearning.AI short courses](https://www.deeplearning.ai/short-courses/)

### Project nên làm

- Agent đọc email, phân loại, draft reply
- Agent tra cứu web + tổng hợp báo cáo
- Agent dùng database tool để trả lời câu hỏi kinh doanh
- Multi-step customer support agent

---

## Giai đoạn 5: LLMOps và Production

**Thời gian:** 2–3 tháng

Đây là phần phân biệt người "biết demo" với người "làm được sản phẩm thật".

### Cần học

**Evaluation**

- Test set cho prompt
- Golden answers
- LLM-as-judge
- Human review
- Regression test cho prompt / model

**Monitoring**

- Log prompt / response
- Latency
- Cost
- Error rate
- User feedback
- Hallucination reports

**Deployment**

- FastAPI service
- Docker
- Background jobs
- Queue: Redis / Celery
- Cloud: AWS / GCP / Azure / Fly.io / Render

**Security**

- Prompt injection
- Data leakage
- API key management
- Rate limit
- PII handling
- Tool permission boundaries

**Nguồn nên học**

- [DeepLearning.AI LLMOps course](https://www.deeplearning.ai/courses/llmops/)

### Project nên làm

- Deploy chatbot RAG có logging, feedback, dashboard cost
- Tạo bộ eval tự động cho chatbot
- Thêm rate limit, auth, prompt injection checks

---

## Giai đoạn 6: Open-source Models và Fine-tuning

**Thời gian:** 2–4 tháng — học sau khi đã vững API / RAG

### Cần học

**Hugging Face ecosystem**

- Transformers
- Tokenizers
- Datasets
- Inference API
- Model Hub

**Fine-tuning căn bản**

- SFT
- LoRA / QLoRA
- Instruction tuning
- Khi nào nên fine-tune, khi nào chỉ cần RAG / prompting

**Model serving**

- vLLM
- TGI
- Ollama cho local dev
- Quantization

### Project nên làm

- Fine-tune model nhỏ cho phân loại intent
- Deploy local LLM API
- So sánh GPT API vs open-source model cho cùng một task

---

## Lộ trình 6 tháng thực tế

| Tháng | Học | Làm |
|-------|-----|-----|
| **1** | Python, Git, FastAPI, SQL, Docker cơ bản | 2 backend project nhỏ |
| **2** | ML căn bản, embeddings, vector search | Semantic search app |
| **3** | OpenAI API (hoặc tương đương), prompting, structured output, tool calling | Chatbot tài liệu đơn giản |
| **4** | RAG nâng cao, vector DB, reranking, citations, evaluation | Knowledge base chatbot hoàn chỉnh |
| **5** | Agents, LangGraph, workflow automation | Agent dùng tools: search, database, email, file |
| **6** | Production, LLMOps, monitoring, security, deployment | Deploy 1 sản phẩm hoàn chỉnh (auth, logs, eval, cost tracking) |

---

## Portfolio nên có

Nếu muốn đi xin việc AI Engineer, bạn nên có **ít nhất 3 project tử tế**:

### 1. RAG Knowledge Assistant

- Upload PDF / documents
- Chat với citation
- Vector DB
- Evaluation
- Deploy online

### 2. AI Agent Workflow

- Agent dùng tools
- Có state / memory
- Có retry / error handling
- Không chỉ là demo chat

### 3. LLM Production App

- FastAPI backend
- Auth
- Logging
- Monitoring cost / latency
- Docker deploy
- Test cases

---

## Thứ tự học khuyến nghị

Nếu bạn đang bắt đầu từ gần số 0:

1. Python
2. Git + terminal
3. FastAPI + SQL
4. ML căn bản
5. Embeddings
6. OpenAI API / LLM API
7. RAG
8. Vector database
9. Agents / tool calling
10. Evaluation
11. Deployment
12. Security
13. Fine-tuning / open-source models

### Không nên học theo thứ tự này lúc đầu

- Đừng lao ngay vào fine-tuning model lớn
- Đừng học quá sâu toán trước khi biết build app
- Đừng chỉ học prompt engineering mà bỏ qua backend
- Đừng chỉ dùng LangChain mà không hiểu RAG / tool calling bên dưới
- Đừng làm chatbot demo không có eval, logging, deployment

---

## Stack gợi ý cho người mới

| Hạng mục | Gợi ý |
|----------|-------|
| Language | Python |
| Backend | FastAPI |
| Database | PostgreSQL |
| Vector DB | Chroma (học), Qdrant hoặc pgvector (nghiêm túc hơn) |
| LLM API | OpenAI API hoặc provider tương đương |
| RAG / Agents | LangGraph, LlamaIndex — dùng vừa đủ |
| Frontend | Streamlit (demo nhanh), Next.js (sản phẩm đẹp) |
| Deploy | Docker + Render / Fly.io / AWS / GCP |
| Monitoring | Logs trước, sau đó thêm tracing / eval tools |

---

> Nếu bạn muốn đi nhanh nhất, hãy học theo hướng **build project trước, lấp kiến thức sau**. Với AI Engineer, portfolio có sản phẩm chạy thật thường giá trị hơn việc chỉ có chứng chỉ.
