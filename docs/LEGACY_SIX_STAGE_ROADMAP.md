# LỘ TRÌNH HỌC AI ENGINEER TỪ CON SỐ 0

> **Bản thiết kế chuẩn thực chiến:** Kết hợp nền tảng Phần mềm, Core ML/DL và Hệ sinh thái GenAI / LLM hiện đại  
> ⏱️ **Thời gian:** 6 – 9 tháng (khoảng 10–12 giờ/tuần) &nbsp;|&nbsp; 🎯 **Mục tiêu:** AI Engineer thực chiến (Production-Ready) &nbsp;|&nbsp; 📌 **Phương pháp:** Software-first, Learn-by-doing (70% Thực hành / 30% Lý thuyết)  
> 📖 **Tài liệu học tập:** [Sổ tay thuật ngữ (GLOSSARY.md)](./docs/GLOSSARY.md) &nbsp;|&nbsp; ⚙️ [Cơ chế hoạt động của AI (AI_OPERATING_MODELS.md)](./docs/AI_OPERATING_MODELS.md) &nbsp;|&nbsp; 🗺️ [Bản đồ các mô hình (AI_MODELS_GUIDE.md)](./docs/AI_MODELS_GUIDE.md)

---

## 🗺️ TỔNG QUAN LỘ TRÌNH 6 GIAI ĐOẠN

| Giai đoạn | Chủ đề trọng tâm | Thời lượng | Đầu ra cốt lõi |
| :--- | :--- | :---: | :--- |
| **Giai đoạn 1** | Python nâng cao, FastAPI, Pydantic, SQL & Database, Git & CLI | 3 – 4 tuần | Xây dựng RESTful Data & CRUD API |
| **Giai đoạn 2** | Toán thực dụng, ML Scikit-Learn & Transformer basics | 4 – 5 tuần | Sentiment Classifier hoàn chỉnh |
| **Giai đoạn 3** | LLM APIs, Prompt Nâng cao, Function Calling, Prompt Caching & Ollama | 2 – 3 tuần | Smart Customer Support Bot |
| **Giai đoạn 4** | RAG Pipeline, Hybrid Search, Vector DB, Reranking & **RAG Evaluation** | 4 – 5 tuần | Enterprise Document Q&A (PDF) kèm Test Suite |
| **Giai đoạn 5** | AI Agents, LangGraph, Multi-Agent & Tool Calling | 3 – 4 tuần | Autonomous Market Research Agent |
| **Giai đoạn 6** | Fine-tuning (LoRA), LLMOps, CI/CD Evaluation & Docker Deploy | 4 – 5 tuần | Production-Ready Domain Assistant |

---

## 🚀 CHI TIẾT CÁC GIAI ĐOẠN

### Giai đoạn 1: Nền tảng Python & Kỹ thuật Phần mềm (3 – 4 tuần)

**🎯 Mục tiêu:** Một AI Engineer giỏi trước hết phải là một Software Engineer vững tay. Bạn cần làm chủ Python, xử lý dữ liệu, thao tác Database và xây dựng RESTful API chuẩn production.

#### 1. Kiến thức cốt lõi:
- **Python nâng cao:** OOP (Lập trình hướng đối tượng), Type Hinting (`typing`), Async/Await (`asyncio`), Generators, Decorators.
- **Môi trường & Quản lý gói:** Virtual environments (`venv`, `poetry` hoặc `uv`), Git & GitHub (Branching, Merge, PR).
- **Cơ sở dữ liệu & ORM:** SQL cơ bản (PostgreSQL/SQLite), kết nối và thao tác dữ liệu an toàn qua ORM (`SQLAlchemy` hoặc `SQLModel`).
- **Xử lý dữ liệu & Text Cleaning:** NumPy (ma trận, vector), Pandas (làm sạch dữ liệu, bảng biểu, aggregation), chuẩn hóa văn bản (Unicode Normalization tiếng Việt, Regex, xóa nhiễu HTML/Markdown).
- **Backend cơ bản:** Xây dựng RESTful API với FastAPI và Pydantic để validate dữ liệu đầu vào/ra chuyên nghiệp.

#### 🛠️ BÀI TẬP THỰC TẾ (PROJECT): Xây dựng File Processing & Analysis Microservice
1. Viết một FastAPI service cho phép người dùng upload file CSV/JSON chứa dữ liệu đơn hàng hoặc người dùng.
2. Dùng Pandas để làm sạch, chuẩn hóa text và thống kê: doanh thu trung bình, top sản phẩm, tỉ lệ churn,...
3. Lưu kết quả phân tích và lịch sử xử lý vào cơ sở dữ liệu PostgreSQL qua SQLAlchemy/SQLModel.
4. Xử lý bất đồng bộ (`asyncio`) nếu file có kích thước lớn để tránh block main thread.
5. Trả kết quả JSON chuẩn hóa qua schema Pydantic. Viết unit test hoàn chỉnh với `pytest`.

---

### Giai đoạn 2: Nền tảng Machine Learning & Deep Learning (4 – 5 tuần)

**🎯 Mục tiêu:** Hiểu bản chất các mô hình học máy và cách hoạt động của mạng nơ-ron (Neural Network) để không coi AI như một 'hộp đen'.

#### 1. Kiến thức cốt lõi:
- **Toán ứng dụng thực chiến:** Đại số tuyến tính (Vector, Dot product, Cosine similarity - nền tảng của Vector Search & Embeddings), Giải tích (Đạo hàm, Gradient Descent), Xác suất thống kê cơ bản.
- **Traditional ML (Scikit-Learn):** Phân loại (Logistic Regression, Random Forest, XGBoost), Đánh giá mô hình (Precision, Recall, F1-Score, ROC-AUC, Confusion Matrix).
- **Deep Learning (PyTorch):** Mạng nơ-ron truyền thẳng (MLP), Hàm mất mát (Loss functions), Tối ưu hóa (Adam, SGD).
- **Kiến trúc Transformer:** Cơ chế Self-Attention, Encoder-Decoder, khái niệm Tokenizer và Embeddings (cực kỳ quan trọng cho các giai đoạn sau).

#### 🛠️ BÀI TẬP THỰC TẾ (PROJECT): Xây dựng hệ thống phân loại cảm xúc phản hồi khách hàng (Sentiment Classifier)
1. Lấy dataset đánh giá (ví dụ: IMDb hoặc review sản phẩm Shopee/Amazon).
2. Tiền xử lý văn bản, tạo text embeddings (dùng TF-IDF trước, sau đó thử với pretrained embedding từ Hugging Face).
3. Huấn luyện một mô hình bằng PyTorch hoặc XGBoost để phân loại (Tích cực / Tiêu cực / Trung lập).
4. Đóng gói mô hình thành một hàm dự đoán, log lại Confusion Matrix và F1-score.

---

### Giai đoạn 3: Làm chủ LLM APIs & Prompt Engineering nâng cao (2 – 3 tuần)

**🎯 Mục tiêu:** Tích hợp các mô hình ngôn ngữ lớn (OpenAI, Gemini, Claude, Llama cục bộ) vào ứng dụng phần mềm một cách tin cậy, có cấu trúc và tối ưu chi phí.

#### 1. Kiến thức cốt lõi:
- **API Foundations:** Chat Completion APIs, Token limits, Context Window, Streaming responses, Parameters (`temperature`, `top_p`, `seed`).
- **Prompt Engineering:** Few-shot prompting, Chain-of-Thought (CoT), ReAct, Role-based prompting.
- **Structured Output:** Ép LLM trả về đúng định dạng JSON/Pydantic schema (Instructor, OpenAI Structured Outputs, Outlines).
- **Function Calling / Tool Use:** Dạy LLM biết khi nào cần gọi hàm ngoài (gọi API thời tiết, tra cứu DB, tính toán).
- **Prompt Caching & Tối ưu chi phí:** Tận dụng tính năng Prompt Caching (Anthropic / OpenAI / Gemini) để giảm 50–80% chi phí token và giảm độ trễ phản hồi.
- **Chạy model local:** Cài đặt và sử dụng Ollama hoặc vLLM để chạy mô hình mã nguồn mở (Llama 3, Qwen, Mistral) trên máy tính cá nhân/GPU.

#### 🛠️ BÀI TẬP THỰC TẾ (PROJECT): Smart Customer Support Bot với Function Calling & Prompt Caching
1. Xây dựng trợ lý ảo hỗ trợ kiểm tra đơn hàng cho sàn thương mại điện tử.
2. Tích hợp Function Calling: Nếu khách hỏi *"Đơn hàng #1234 của tôi bao giờ tới?"*, LLM tự nhận diện intent và gọi hàm `get_order_status(order_id='1234')` từ database giả lập.
3. Kích hoạt Prompt Caching cho phần System Instructions dài để tối ưu chi phí.
4. Output luôn trả về dạng JSON có cấu trúc gồm: `intent`, `message_to_user`, `action_taken`.

---

### Giai đoạn 4: RAG (Retrieval-Augmented Generation), Vector DB & Evaluation (4 – 5 tuần)

**🎯 Mục tiêu:** Giải quyết bài toán lớn nhất của doanh nghiệp: Đưa dữ liệu nội bộ (PDF, Word, Notion, SQL) vào LLM mà không cần train lại model, hạn chế hallucination (bịa đặt thông tin) và **đo lường độ chính xác bằng số liệu cụ thể (Evaluation)**.

#### 1. Kiến thức cốt lõi:
- **Quy trình RAG cơ bản:** Ingestion ➔ Chunking (Fixed-size, Recursive, Semantic) ➔ Embedding (OpenAI `text-embedding-3`, BGE, Nomic) ➔ Vector Storage ➔ Retrieval ➔ Generation.
- **Vector Databases:** Hiểu và thực hành thành thạo với ChromaDB, Qdrant hoặc pgvector (PostgreSQL).
- **Advanced RAG (RAG nâng cao):** Các kỹ thuật tối ưu độ chính xác:
  - **Hybrid Search:** Kết hợp Dense Retrieval (Vector search) + Sparse Retrieval (BM25 / Keyword search).
  - **Re-ranking:** Dùng mô hình Cross-Encoder (như Cohere Rerank, BGE-Reranker) để lọc lại top kết quả phù hợp nhất.
  - **Query Transformation:** Rewrite query, Multi-query generation, HyDE (Hypothetical Document Embeddings).
  - **Document Parsing:** Trích xuất bảng biểu, cấu trúc văn bản từ PDF (LlamaParse, Marker, Unstructured).
- **RAG Evaluation (Đánh giá định lượng):** Tránh cái bẫy "Vibe Check" (chỉ thử bằng mắt vài câu):
  - Xây dựng **Ground Truth Test Set** (bộ 30 – 50 câu hỏi có sẵn đáp án chuẩn và tài liệu trích dẫn).
  - Đo lường chỉ số tìm kiếm: **Hit Rate**, **MRR** (Mean Reciprocal Rank).
  - Đo lường chất lượng câu trả lời bằng **Ragas** hoặc **LLM-as-a-judge**: **Faithfulness** (độ trung thực, chống hallucination), **Answer Relevance** (độ trúng trọng tâm), **Context Precision/Recall** (chất lượng đoạn trích xuất).
- **Semantic Caching:** Sử dụng Redis để lưu cache các câu hỏi tương đồng ngữ nghĩa, trả kết quả ngay lập tức mà không cần gọi lại LLM.

#### 🛠️ BÀI TẬP THỰC TẾ (PROJECT): Trợ lý tra cứu tài liệu doanh nghiệp kèm Evaluation Test Suite
1. Ingest kho tài liệu (tối thiểu 5 file PDF dài chứa bảng biểu, điều khoản).
2. Áp dụng Recursive Chunking + Pretrained Vietnamese/Multilingual Embedding.
3. Cài đặt Hybrid Search (BM25 + Vector) và Re-ranking để tăng độ chính xác.
4. Tích hợp Semantic Cache (Redis) cho các câu hỏi phổ biến.
5. **Chạy Evaluation Suite:** Tự tạo bộ test 30 câu hỏi, chạy đo điểm qua Ragas và xuất báo cáo so sánh: RAG cơ bản vs RAG nâng cao (chứng minh điểm Faithfulness tăng > 15%).
6. Giao diện: Hiển thị câu trả lời kèm Citation (trích dẫn chính xác tên tài liệu, số trang hoặc đoạn văn bản gốc).

---

### Giai đoạn 5: AI Agents & Hệ thống Tự hành (3 – 4 tuần)

**🎯 Mục tiêu:** Xây dựng hệ sinh thái AI có khả năng tự lập kế hoạch (Planning), suy luận qua nhiều bước (Multi-step Reasoning), sử dụng công cụ và ghi nhớ bối cảnh (Long-term Memory).

#### 1. Kiến thức cốt lõi:
- **Kiến trúc Agent:** ReAct framework (Reasoning + Acting), Plan-and-Solve, Reflection / Self-Correction.
- **Frameworks:** LangGraph (Xây dựng Agent dưới dạng đồ thị trạng thái tuần hoàn Stateful Graph – chuẩn công nghiệp hiện nay), LlamaIndex / CrewAI (Phù hợp cho multi-agent collaboration).
- **Bộ nhớ (Memory):** Short-term (in-context window), Long-term (Semantic Memory dùng Vector Store / SQL).
- **Human-in-the-loop (HITL):** Cơ chế dừng lại để con người duyệt trước khi Agent thực hiện các hành động nhạy cảm (như gửi email, xóa DB, thanh toán).

#### 🛠️ BÀI TẬP THỰC TẾ (PROJECT): Tự động hóa nghiên cứu thị trường (Automated Market Research Agent)
1. Người dùng nhập tên một công ty hoặc sản phẩm (ví dụ: *"Phân tích xu hướng xe điện VinFast"*).
2. **Agent 1 (Searcher):** Tự động tìm kiếm web (dùng DuckDuckGo / Tavily API), tổng hợp các bài báo gần nhất.
3. **Agent 2 (Analyst):** Đọc nội dung, trích xuất điểm mạnh, điểm yếu, đối thủ cạnh tranh.
4. **Agent 3 (Writer):** Tổng hợp thành báo cáo Markdown hoàn chỉnh kèm bảng biểu so sánh.
5. Xây dựng bằng LangGraph có quản lý state và xử lý lỗi fallback nếu một link bị chết.

---

### Giai đoạn 6: Fine-tuning, LLMOps & Đưa vào Production (4 – 5 tuần)

**🎯 Mục tiêu:** Đưa ứng dụng AI từ notebook ra môi trường thật với độ trễ thấp, chi phí tối ưu, có giám sát tự động và đảm bảo an toàn.

#### 1. Kiến thức cốt lõi:
- **Fine-tuning (Tinh chỉnh mô hình):** Khi nào nên dùng RAG, khi nào nên Fine-tune? Kỹ thuật PEFT / LoRA, QLoRA (huấn luyện tham số hiệu quả trên GPU vừa). Thư viện: Hugging Face transformers, peft, trl, hoặc Unsloth.
- **CI/CD Evaluation & LLM Testing:** Tự động chạy test suite đo lường độ chính xác (Ragas, DeepEval) mỗi khi cập nhật prompt/model trước khi merge code vào production.
- **LLMOps & Giám sát (Observability):** Tracing toàn bộ luồng gọi, đo token tiêu thụ, latency, chi phí thực tế: LangSmith, Phoenix (Arize), hoặc OpenTelemetry.
- **Bảo mật AI (AI Safety):** Ngăn chặn Prompt Injection, Jailbreak, rò rỉ PII (thông tin cá nhân) bằng Guardrails (NeMo Guardrails, Llama Guard).
- **Triển khai (Deployment):** Đóng gói Docker, cấu hình vLLM trên Cloud GPU (RunPod, Modal, AWS SageMaker) để tối ưu throughput với PagedAttention.

#### 🛠️ BÀI TẬP THỰC TẾ (PROJECT): Production-ready Legal or Medical Assistant (Capstone Project)
1. Tự chuẩn bị bộ dữ liệu domain chuyên ngành (ví dụ: Luật lao động hoặc Y tế cơ bản).
2. Sử dụng LoRA/QLoRA để fine-tune một model nhỏ (như Llama 3 8B hoặc Qwen 2.5 7B) theo phong cách trả lời chuyên gia.
3. Kết hợp hệ thống RAG để cập nhật các văn bản mới nhất.
4. Thiết lập pipeline đánh giá tự động (Evaluation Test Suite) đo lường độ chính xác (Ragas score > 0.85).
5. Đóng gói Docker, tích hợp LangSmith để track log và deploy API có rate limit, caching (Redis).

---

## 💻 BỘ CÔNG CỤ (TECH STACK) CẦN LÀM CHỦ

| Mảng kỹ năng | Công nghệ / Thư viện đề xuất | Vai trò trong hệ thống |
| :--- | :--- | :--- |
| **Ngôn ngữ & Backend** | Python 3.11+, FastAPI, Pydantic, Poetry/uv | Xây dựng core logic, xử lý dữ liệu và REST API chuẩn |
| **Database & ORM** | PostgreSQL, SQLite, SQLAlchemy / SQLModel | Lưu trữ dữ liệu quan hệ, lịch sử chat và metadata |
| **Core ML & DL** | Scikit-Learn, PyTorch, Hugging Face Transformers | Nắm bản chất thuật toán, text embedding và attention |
| **LLM Orchestration** | LangGraph, LlamaIndex, Instructor | Điều phối flow gọi model, quản lý state và ép kiểu JSON |
| **Vector DB & Search** | Qdrant, ChromaDB, pgvector (PostgreSQL) | Lưu trữ vector embeddings, tìm kiếm tương đồng ngữ nghĩa |
| **Caching & Tối ưu** | Redis (Semantic Cache), Provider Prompt Caching | Giảm 50–80% chi phí gọi API và tăng tốc độ phản hồi |
| **Evaluation & Tracing** | Ragas, DeepEval, LangSmith, Phoenix | Đo lường độ chính xác (RAG metric), track log, latency |
| **Inference & Fine-tuning** | Ollama, vLLM, Unsloth, PEFT / LoRA | Chạy model local tốc độ cao, tinh chỉnh model chuyên ngành |
| **DevOps & Cloud** | Docker, Git, RunPod / Modal, AWS / GCP | Đóng gói container, CI/CD và triển khai ứng dụng lên cloud |

---

## 💡 4 NGUYÊN TẮC VÀNG ĐỂ HỌC HIỆU QUẢ

- 🎯 **1. Đừng học vẹt lý thuyết (Learn by Building):** Áp dụng nguyên tắc 70/30 (70% thời gian thực hành code và debug, 30% lý thuyết). Viết 10 dòng code gọi API và xử lý lỗi thực tế sẽ nhớ lâu hơn đọc 5 bài blog.
- 📊 **2. Nói chuyện bằng số liệu, bỏ qua "Vibe Check":** Không bao giờ kết luận model tốt chỉ bằng 3–5 câu test thử. Hãy tạo bộ Ground Truth Test Set và đo lường bằng số liệu (Accuracy, Faithfulness, Hit Rate).
- 🚀 **3. Xây dựng 'Proof of Concept' công khai:** Mỗi bài tập sau khi hoàn thành, hãy push lên GitHub kèm file `README.md` giải thích kiến trúc, sơ đồ luồng (flowchart) và video demo 1 phút. Đây chính là chiếc CV thuyết phục nhất khi đi phỏng vấn.
- 💼 **4. Tư duy hướng sản phẩm & Tối ưu chi phí:** Một AI Engineer giỏi không phải là người dùng model to nhất hay đắt nhất, mà là người biết chọn model nhỏ nhất, rẻ nhất, dùng cache hiệu quả nhưng vẫn giải quyết đúng bài toán của người dùng.

> 🌟 **Hành trình trở thành AI Engineer đòi hỏi sự kiên trì và thực hành liên tục. Hãy bắt đầu ngay từ những dòng code nhỏ nhất hôm nay!**
