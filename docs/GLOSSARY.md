# 📖 SỔ TAY THUẬT NGỮ AI ENGINEER (GLOSSARY)

> Cuốn cẩm nang tra cứu toàn diện các khái niệm, công nghệ và thuật ngữ cốt lõi dành cho AI Engineer thực chiến. Được biên soạn theo phong cách dễ hiểu, có ví dụ thực tế và giải thích bản chất kỹ thuật.  
> ⚙️ **Cơ chế hoạt động:** Xem cách AI thực sự hoạt động bên trong (Under the hood) tại [Cơ chế hoạt động của AI (AI_OPERATING_MODELS.md)](./AI_OPERATING_MODELS.md)  
> 🗺️ **Bản đồ các mô hình:** Xem cách phối hợp các mô hình thực tế tại [Bản đồ các mô hình AI thực chiến (AI_MODELS_GUIDE.md)](./AI_MODELS_GUIDE.md)

---

## 📑 MỤC LỤC
1. [Bản chất LLM & Xử lý Ngôn ngữ](#1-bản-chất-llm--xử-lý-ngôn-ngữ)
2. [Kỹ thuật Prompt & Lập trình API](#2-kỹ-thuật-prompt--lập-trình-api)
3. [RAG & Tìm kiếm Thông minh (Retrieval)](#3-rag--tìm-kiếm-thông-minh-retrieval)
4. [AI Agents & Hệ thống Tự hành](#4-ai-agents--hệ-thống-tự-hành)
5. [Đánh giá & Kiểm thử AI (Evaluation)](#5-đánh-giá--kiểm-thử-ai-evaluation)
6. [Mô hình Mã nguồn mở, Fine-tuning & LLMOps](#6-mô-hình-mã-nguồn-mở-fine-tuning--llmops)

---

## 1. BẢN CHẤT LLM & XỬ LÝ NGÔN NGỮ

### Token & Tokenizer
- **Khái niệm:** Máy tính không xử lý văn bản theo từng chữ cái hay từng từ nguyên vẹn. **Tokenizer** là công cụ phân rã câu chữ thành các mảnh nhỏ gọi là **Tokens** (có thể là một từ, một phần của từ, hoặc ký tự đặc biệt).
- **Ví dụ:** Từ `"ChatGPT"` thường được tách thành 2 tokens: `["Chat", "GPT"]`. Trong tiếng Việt có dấu, một từ có thể tốn từ 1 đến 3 tokens tùy theo bộ mã tokenizer của từng model.
- **Tại sao cần biết:** Các nhà cung cấp API (OpenAI, Anthropic, Google) tính tiền theo số lượng token gửi vào (Input) và sinh ra (Output).

### Context Window (Cửa sổ ngữ cảnh)
- **Khái niệm:** Là dung lượng bộ nhớ tối đa (tính theo số tokens) mà một mô hình LLM có thể tiếp nhận và ghi nhớ trong một phiên xử lý duy nhất.
- **Ví dụ:** Model GPT-4o có context window là 128k tokens (~300 trang sách), Gemini 1.5 Pro có context window lên tới 1 triệu tokens (vài cuốn tiểu thuyết hoặc 1 giờ video).
- **Lưu ý:** Context window càng lớn thì chi phí càng cao và tốc độ phản hồi có thể chậm hơn.

### Embedding (Vectơ hóa ngữ nghĩa)
- **Khái niệm:** Là quá trình chuyển đổi một đoạn văn bản thành một **dãy số thực (Vector)** có số chiều cố định (ví dụ: 1536 chiều với OpenAI `text-embedding-3`).
- **Bản chất:** Các đoạn văn bản có nội dung/ngữ nghĩa tương đồng sẽ có tọa độ không gian nằm gần nhau.
  - *Ví dụ:* Tọa độ của *"chó"* sẽ gần *"mèo"* hơn là *"máy giặt"*.
- **Ứng dụng:** Là nền tảng bắt buộc để thực hiện tìm kiếm thông minh (Semantic Search) trong hệ thống RAG.

### Hallucination (Ảo giác / Bịa đặt)
- **Khái niệm:** Hiện tượng LLM tạo ra các thông tin sai sự thật, không có thật trong dữ liệu nguồn nhưng được hành văn một cách cực kỳ mạch lạc, tự tin và trôi chảy.
- **Giải pháp:** Sử dụng kỹ thuật RAG (cung cấp tài liệu làm căn cứ), hạ `temperature` về 0, áp dụng Guardrails và kỹ thuật kiểm tra chéo (Evaluation).

### Temperature, Top-P, Seed
- **Temperature (0.0 đến 2.0):** Tham số điều khiển độ sáng tạo / ngẫu nhiên của câu trả lời.
  - `0.0`: Trả lời an toàn, nhất quán, logic (phù hợp cho trích xuất JSON, code, toán học, RAG).
  - `0.7 – 1.0`: Trả lời tự nhiên, đa dạng (phù hợp cho viết lách, sáng tạo nội dung, chatbot trò chuyện).
- **Top-P (Nucleus Sampling):** Giới hạn tập từ vựng tiềm năng theo tổng xác suất tích lũy. Thường khuyến nghị chỉ chỉnh một trong hai: hoặc `temperature` hoặc `top_p`.
- **Seed:** Đặt số nguyên cố định để đảm bảo kết quả trả về giữa các lần gọi có tính lặp lại (hữu ích khi viết Unit Test).

### Transformer & Attention Mechanism
- **Transformer:** Kiến trúc mạng nơ-ron nền tảng làm nên cuộc cách mạng GenAI hiện đại (công bố năm 2017 bởi Google trong bài báo kinh điển *"Attention Is All You Need"*).
- **Self-Attention:** Cơ chế giúp mô hình khi đọc một từ có thể "chú ý" đến các từ liên quan khác trong câu để hiểu đúng ngữ cảnh.
  - *Ví dụ:* Trong câu *"Con vật không qua được đường vì **nó** quá mệt"*, cơ chế Attention giúp mô hình hiểu chữ **"nó"** đang chỉ **"con vật"** chứ không phải "con đường".

---

## 2. KỸ THUẬT PROMPT & LẬP TRÌNH API

### Prompt Engineering
- **Khái niệm:** Kỹ thuật thiết kế câu lệnh đầu vào để hướng dẫn LLM trả về kết quả chính xác, đúng định dạng và tối ưu nhất.
- **Các kỹ thuật thông dụng:**
  - **Few-shot Prompting:** Đưa kèm 2–3 ví dụ mẫu (câu hỏi + câu trả lời mẫu) vào prompt để model bắt chước định dạng.
  - **Chain-of-Thought (CoT):** Yêu cầu model "hãy suy nghĩ từng bước một" (Think step-by-step) trước khi đưa ra kết quả cuối cùng, giúp tăng độ chính xác trong các bài toán logic/toán học.
  - **Role-based Prompting:** Gán vai trò cụ thể cho AI (ví dụ: *"Bạn là một luật sư lao động 10 năm kinh nghiệm..."*).

### Structured Output & Pydantic
- **Khái niệm:** Kỹ thuật ép buộc mô hình LLM phải trả về dữ liệu tuân thủ 100% theo cấu trúc JSON định sẵn (thay vì văn bản tự do).
- **Tại sao cần:** Trong lập trình phần mềm, backend không thể phân tích một đoạn văn xuôi tùy hứng. Bắt buộc phải có JSON chuẩn để lưu Database hoặc gọi API khác.
- **Công cụ:** Pydantic (trong Python), OpenAI Structured Outputs, thư viện `instructor`.

### Function Calling (Tool Use)
- **Khái niệm:** Cơ chế cho phép LLM giao tiếp với thế giới bên ngoài. Khi người dùng hỏi một thông tin mà LLM không biết hoặc cần hành động thực tế, LLM sẽ sinh ra một lệnh gọi hàm chứa các tham số cần thiết để code phần mềm của bạn thực thi.
- **Quy trình:**
  1. Người dùng: *"Đơn hàng #8899 của tôi đang ở đâu?"*
  2. LLM phát hiện cần dữ liệu ngoài ➔ trả về: `call get_order_status(order_id="8899")`.
  3. Backend Python chạy hàm, truy vấn Database lấy kết quả: `{"status": "Đang giao", "shipper": "0987xxx"}`.
  4. Backend gửi kết quả này lại cho LLM để nó tổng hợp câu trả lời tự nhiên cho khách.

### Prompt Caching & Semantic Caching
- **Prompt Caching:** Tính năng của các nhà cung cấp API (Claude, OpenAI, Gemini) tự động lưu vào bộ nhớ đệm những đoạn prompt dài được dùng lại nhiều lần (như System prompt, kho tài liệu mẫu). Giúp giảm đến 80% chi phí tiền token và tăng tốc độ trả về gấp 2–4 lần.
- **Semantic Caching:** Kỹ thuật do lập trình viên tự cài đặt (dùng Redis/Vector DB). Khi người dùng hỏi một câu tương tự về mặt ý nghĩa với câu hỏi cũ trong quá khứ, hệ thống trả về kết quả lưu sẵn trong cache ngay lập tức (dưới 10ms) mà không tốn 1 xu gọi LLM.

---

## 3. RAG & TÌM KIẾM THÔNG MINH (RETRIEVAL)

### RAG (Retrieval-Augmented Generation)
- **Khái niệm:** Kiến trúc kết hợp giữa **Hệ thống tìm kiếm thông tin** (Retrieval) và **Mô hình sinh ngôn ngữ** (Generation).
- **Cơ chế:** Khi có câu hỏi, hệ thống đi tìm các đoạn văn bản có liên quan trong kho dữ liệu nội bộ, sau đó "dán" các đoạn văn đó vào prompt làm căn cứ để LLM đọc và trả lời.

### Chunking (Phân mảnh tài liệu)
- **Khái niệm:** Kỹ thuật chia nhỏ tài liệu lớn (sách, PDF) thành các đoạn văn nhỏ có kích thước phù hợp (chunk size) kèm một phần gối đầu lên nhau (chunk overlap).
- **Các chiến lược:**
  - *Fixed-size:* Cắt đều mỗi đoạn 500 ký tự (đơn giản nhưng dễ cắt ngang câu).
  - *Recursive:* Cắt theo dấu đoạn văn (`\n\n`), dấu xuống dòng (`\n`), dấu chấm câu (giữ trọn vẹn ngữ nghĩa câu).
  - *Semantic Chunking:* Cắt dựa vào sự thay đổi ý nghĩa giữa các câu (dùng embedding để nhận biết).

### Vector Database
- **Khái niệm:** Hệ quản trị cơ sở dữ liệu chuyên biệt để lưu trữ các Vector Embedding và hỗ trợ thuật toán tìm kiếm láng giềng gần nhất (ANN - Approximate Nearest Neighbors).
- **Các hệ thống phổ biến:** Qdrant, ChromaDB, Milvus, Pinecone, hoặc extension `pgvector` trên PostgreSQL.

### Dense Retrieval vs Sparse Retrieval & Hybrid Search
- **Sparse Retrieval (Tìm kiếm thưa / từ khóa):** Sử dụng thuật toán đếm tần suất xuất hiện của từ (như TF-IDF, BM25). Rất mạnh khi tìm chính xác mã sản phẩm, số điện thoại, tên riêng, thuật ngữ kỹ thuật.
- **Dense Retrieval (Tìm kiếm đặc / ngữ nghĩa):** Sử dụng Vector Embeddings để tìm kiếm theo ý nghĩa và từ đồng nghĩa.
- **Hybrid Search (Tìm kiếm lai):** Kết hợp cả hai phương pháp trên lại với nhau để vừa không bỏ sót từ khóa kỹ thuật, vừa hiểu được ngữ nghĩa câu hỏi.

### Re-ranking (Tái xếp hạng)
- **Khái niệm:** Sau khi Hybrid Search tìm ra khoảng 20–50 tài liệu tiềm năng, một mô hình nhỏ chuyên biệt (Cross-Encoder như Cohere Rerank, BGE-Reranker) sẽ chấm điểm lại mối quan hệ giữa câu hỏi và từng đoạn văn, chọn ra top 3–5 đoạn văn đắt giá nhất.
- **Lợi ích:** Tăng vọt độ chính xác của RAG và giảm lượng token rác đưa vào LLM.

### HyDE (Hypothetical Document Embeddings)
- **Khái niệm:** Khi câu hỏi của người dùng quá ngắn (ví dụ: *"nghỉ phép"*), tìm kiếm vector thường kém hiệu quả. Kỹ thuật HyDE sẽ yêu cầu LLM "bịa" ra một câu trả lời giả định. Sau đó dùng chính câu trả lời giả định này đi tìm kiếm trong kho tài liệu. Đoạn tài liệu thật thường sẽ có độ tương đồng rất cao với câu trả lời giả định.

---

## 4. AI AGENTS & HỆ THỐNG TỰ HÀNH

### AI Agent
- **Khái niệm:** Một chương trình AI có tính tự chủ, được trang bị:
  1. **Khả năng suy luận (Reasoning/Planning):** Biết chia nhỏ mục tiêu phức tạp thành các bước.
  2. **Công cụ (Tools):** Biết gọi API, duyệt web, truy vấn DB.
  3. **Bộ nhớ (Memory):** Nhớ các thông tin trong quá khứ.
  4. **Vòng lặp hành động (Action Loop):** Thực hiện ➔ Kiểm tra kết quả ➔ Nếu sai thì thử cách khác.

### ReAct Framework (Reason + Act)
- **Khái niệm:** Mẫu thiết kế phổ biến nhất cho Agent: Mô hình liên tục lặp lại chu trình: **Thought** (Suy nghĩ xem cần làm gì) ➔ **Action** (Thực hiện hành động bằng công cụ) ➔ **Observation** (Quan sát kết quả trả về từ công cụ) ➔ Đưa ra quyết định tiếp theo.

### LangGraph & Stateful Graph
- **Khái niệm:** Framework của LangChain giúp xây dựng Agent dưới dạng **Đồ thị trạng thái tuần hoàn (Stateful Multi-Actor Graph)**.
- **Ưu điểm vượt trội:** Thay vì để Agent chạy tự do không kiểm soát (dễ rơi vào vòng lặp vô tận hoặc tốn tiền vô ích), LangGraph định nghĩa rõ các Node (bước xử lý) và Edge (điều kiện rẽ nhánh), giúp hệ thống ổn định và dự đoán được (deterministic).

### Human-in-the-loop (HITL)
- **Khái niệm:** Cơ chế tạm dừng quy trình tự động của Agent tại các bước có rủi ro cao (chuyển tiền, xóa database, gửi email cho khách) để yêu cầu người dùng xác nhận hoặc chỉnh sửa trước khi Agent được phép tiếp tục.

---

## 5. ĐÁNH GIÁ & KIỂM THỬ AI (EVALUATION)

### Vibe Check vs Quantitative Evaluation
- **Vibe Check (Đoán mò cảm tính):** Người lập trình tự gõ thử 3–5 câu, thấy trả lời trơn tru rồi cho rằng hệ thống đã hoàn thiện. Đây là nguyên nhân số 1 dẫn đến thất bại khi đưa AI vào sản xuất.
- **Quantitative Evaluation (Đánh giá định lượng):** Chạy kiểm thử tự động trên một tập hợp hàng chục/hàng trăm câu hỏi mẫu và xuất ra các chỉ số phần trăm chính xác rõ ràng.

### Ground Truth Test Set
- **Khái niệm:** Bộ dữ liệu kiểm thử chuẩn gồm danh sách các câu hỏi thực tế, đi kèm tài liệu tham chiếu chuẩn xác và câu trả lời hoàn hảo do chuyên gia con người biên soạn để làm thước đo chấm điểm cho AI.

### LLM-as-a-Judge
- **Khái niệm:** Phương pháp sử dụng một mô hình LLM cao cấp (như GPT-4o, Claude 3.5 Sonnet) đóng vai trò giám khảo, đọc câu trả lời của hệ thống AI bạn viết và chấm điểm dựa trên một bộ tiêu chí nghiêm ngặt (Rubric).

### Ragas Metrics (Bộ chỉ số đánh giá RAG)
- **Faithfulness (Độ trung thực):** Đo xem có bao nhiêu thông tin trong câu trả lời bắt nguồn trực tiếp từ tài liệu tìm được (chống Hallucination).
- **Answer Relevance (Độ liên quan):** Đo xem câu trả lời có đi thẳng vào trọng tâm câu hỏi của người dùng hay không.
- **Context Precision:** Đo xem trong các đoạn văn mà bộ tìm kiếm lấy về, đoạn chứa đáp án có nằm ở vị trí đầu tiên hay không.
- **Context Recall:** Đo xem bộ tìm kiếm có tìm đủ toàn bộ thông tin cần thiết để trả lời câu hỏi hay không.

### Hit Rate & MRR (Mean Reciprocal Rank)
- **Hit Rate:** Tỷ lệ phần trăm các lần tìm kiếm mà tài liệu đúng nằm trong Top K kết quả đầu tiên.
- **MRR:** Chỉ số đo lường vị trí của tài liệu đúng (nằm ở vị trí thứ 1 điểm sẽ cao hơn nhiều so với nằm ở vị trí thứ 5).

---

## 6. MÔ HÌNH MÃ NGUỒN MỞ, FINE-TUNING & LLMOPS

### Open-source LLM
- **Khái niệm:** Các mô hình ngôn ngữ lớn được công khai trọng số (weights) cho phép tải về và chạy tự do trên hạ tầng riêng mà không phụ thuộc vào OpenAI hay Google (Ví dụ: Llama 3 của Meta, Qwen của Alibaba, Mistral của Pháp).

### Ollama vs vLLM
- **Ollama:** Công cụ đơn giản, đóng gói sẵn giúp người dùng chạy mô hình local trên macOS, Linux, Windows chỉ bằng 1 dòng lệnh (`ollama run llama3`). Rất tốt cho việc phát triển và thử nghiệm cục bộ.
- **vLLM:** Thư viện phục vụ mô hình (Model Serving) hiệu năng cao cho môi trường Production, hỗ trợ kỹ thuật **PagedAttention** giúp tăng tốc độ xử lý đồng thời lên 10–20 lần trên máy chủ GPU.

### Fine-tuning, PEFT & LoRA
- **Fine-tuning (Tinh chỉnh mô hình):** Huấn luyện tiếp một mô hình đã có sẵn với dữ liệu chuyên biệt để thay đổi phong cách hành văn hoặc học sâu vào một nghiệp vụ cụ thể.
- **PEFT (Parameter-Efficient Fine-Tuning):** Kỹ thuật tinh chỉnh tham số hiệu quả, không cần cập nhật toàn bộ tham số của model.
- **LoRA (Low-Rank Adaptation):** Phương pháp PEFT phổ biến nhất: Giữ nguyên trọng số gốc của mô hình, chỉ chèn thêm các ma trận nhỏ vào từng lớp để huấn luyện. Giúp bạn có thể fine-tune mô hình 8B–14B tham số trên một chiếc GPU tầm trung với chi phí cực thấp.

### LLMOps & Observability (Giám sát)
- **Khái niệm:** Tập hợp các công cụ và quy trình vận hành ứng dụng LLM trong môi trường thực tế (tương tự DevOps trong phần mềm).
- **Tracing (Truy vết):** Ghi lại chi tiết từng bước: người dùng gửi prompt gì, hệ thống tìm ra tài liệu nào, gọi tool gì, tốn bao nhiêu token, phản hồi mất bao nhiêu giây (Công cụ phổ biến: LangSmith, Arize Phoenix, OpenTelemetry).
- **AI Guardrails:** Các lớp phòng thủ tự động đặt ở đầu vào và đầu ra nhằm ngăn chặn tấn công Prompt Injection, Jailbreak hoặc chặn AI tiết lộ thông tin nhạy cảm (PII).

---

> 💡 **Mẹo học tập:** Khi gặp bất kỳ từ khóa nào trong quá trình làm bài tập thực tế, hãy quay lại tra cứu file này để nắm chắc bản chất trước khi bắt tay vào viết code!
