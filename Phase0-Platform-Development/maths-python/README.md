# Maths for AI Engineer

Bộ tài liệu này là lộ trình toán nền tảng cho người học AI Engineer bằng Python.
Nó không chỉ giải thích công thức, mà còn trả lời câu hỏi quan trọng hơn: học phần này
để hiểu điều gì trong machine learning, deep learning và generative AI.

## Cách Học

Mỗi chương được viết theo cùng một cấu trúc:

1. Mục tiêu học
2. Bức tranh lớn
3. Khái niệm cốt lõi
4. Ví dụ tính tay
5. Python Lab
6. Ứng dụng trong AI
7. Lỗi hay nhầm
8. Bài tập
9. Checklist cần nhớ

Bạn nên đọc bằng mắt trước, sau đó mới chạy code. Toán cho AI không phải học thuộc công
thức thật nhiều; quan trọng là nhìn thấy công thức đang mô tả hành vi nào của dữ liệu
hoặc model.

## Lộ Trình Đề Xuất

### 1. Linear Algebra

File: [linear-algebra.md](./linear-algebra.md)

Học để hiểu:

- Vector, matrix và tensor là gì.
- Vì sao câu văn, ảnh, user, sản phẩm đều có thể biến thành vector.
- Dot product, norm và cosine similarity dùng thế nào trong embedding search.
- Matrix multiplication là nền tảng của neural network.

Ứng dụng AI:

- Embedding
- Semantic search
- Recommendation system
- Linear layer trong neural network

### 2. Statistics

File: [statistics.md](./statistics.md)

Học để hiểu:

- Dữ liệu nằm quanh đâu và phân tán ra sao.
- Mean, median, variance, standard deviation khác nhau thế nào.
- Correlation giúp đọc quan hệ giữa feature và target ra sao.
- Sampling giúp đánh giá nhanh dữ liệu lớn như thế nào.

Ứng dụng AI:

- Exploratory data analysis
- Feature engineering
- Data cleaning
- Model evaluation

### 3. Probability

File: [probability.md](./probability.md)

Học để hiểu:

- AI xử lý sự không chắc chắn bằng xác suất.
- Distribution, random variable và conditional probability là gì.
- Bayes giúp cập nhật niềm tin khi có bằng chứng mới.
- Cross-entropy liên quan trực tiếp đến classification loss.

Ứng dụng AI:

- Spam classifier
- Softmax output
- Cross-entropy loss
- Language model sampling
- Uncertainty estimation

### 4. Gradient and Optimization

File: [gradient.md](./gradient.md)

Học để hiểu:

- Đạo hàm và gradient cho biết loss thay đổi theo tham số ra sao.
- Gradient descent giúp model học từ lỗi.
- Learning rate ảnh hưởng mạnh đến quá trình train model.
- PyTorch dùng autograd để tự động tính gradient.

Ứng dụng AI:

- Linear regression
- Neural network training
- Backpropagation
- Optimizer như SGD và Adam

## Quy Tắc Học Hiệu Quả

- Đừng cố nhớ công thức trước khi hiểu trực giác.
- Với mỗi công thức, hãy tự hỏi: đại lượng này đang đo cái gì?
- Với mỗi đoạn Python, hãy tự hỏi: dòng code này tương ứng với công thức nào?
- Với mỗi ví dụ AI, hãy tự hỏi: nếu dữ liệu thật lớn hơn 1 triệu lần thì ý tưởng này còn dùng được không?

## Gợi Ý Nhịp Học

Nếu mỗi ngày học 60-90 phút:

```text
Ngày 1-2: Linear Algebra
Ngày 3-4: Statistics
Ngày 5-6: Probability
Ngày 7-8: Gradient and Optimization
Ngày 9: Làm lại bài tập và viết notebook riêng
Ngày 10: Áp dụng vào một mini project
```

Mini project phù hợp sau 4 chương:

- Tìm câu hỏi giống nhau bằng cosine similarity.
- Phân tích dữ liệu nhà đất giả bằng statistics.
- Viết spam classifier đơn giản.
- Train linear regression bằng gradient descent tự viết.

