# 1. Vector là gì? (HÌNH HỌC)
# Vector = một mảng số, biểu diễn một điểm hoặc một hướng trong không gian.

# Ví dụ:

# v = [3, 4] là vector 2 chiều (x=3, y=4)

# w = [1, 2, 3] là vector 3 chiều

# Trong AI: mỗi câu, mỗi từ, mỗi bức ảnh đều có thể biểu diễn thành vector (gọi là embedding).



# Dot Product (Tích vô hướng)
# Dot Product = tổng của tích các phần tử tương ứng của 2 vector.
# Công thức : a · b = a1*b1 + a2*b2 + a3*b3 + ...
# Ví dụ:

# v = [3, 4]
# w = [1, 2]

# dot_product = 3*1 + 4*2 = 11

# Trong AI: tính toán độ tương đồng giữa 2 vector.

# Ví dụ: tính toán độ tương đồng giữa 2 câu:

# câu 1: "Tôi thích đọc sách"
# câu 2: "Tôi thích đọc báo"

# vector câu 1: [1, 1, 1, 1, 1]
# vector câu 2: [1, 1, 1, 1, 1]

# dot_product = 1*1 + 1*1 + 1*1 + 1*1 + 1*1 = 5

# độ tương đồng = dot_product / (len(vector câu 1) * len(vector câu 2)) = 5 / (5 * 5) = 0.2

import numpy as np

a = np.array([1, 2])
b = np.array([3, 4])

# Cách 1: dùng numpy
dot_product = np.dot(a, b)
print(f"Dot product: {dot_product}")  # 11

# Cách 2: tính tay trong Python
manual_dot = sum(a_i * b_i for a_i, b_i in zip(a, b))
print(f"Manual: {manual_dot}")  # 11

# Ý nghĩa:

# Dot product càng lớn → 2 vector cùng hướng (giống nhau)

# Dot product = 0 → 2 vector vuông góc (không liên quan)


# “Không liên quan” nghĩa là gì?

# Trong toán/AI:

# vector thường biểu diễn đặc trưng/thông tin

# Ví dụ AI embedding:

# Vector	Ý nghĩa
# A	         “mèo”
# B	         “chó”
# C	         “database SQL”

# Thì:

# A và B có thể khá cùng hướng → liên quan động vật
# A và C gần vuông góc → gần như không liên quan



# Độ dài vector (Norm / L2 Norm)
# Độ dài vector = căn bậc hai của tổng bình phương các phần tử.
# Công thức: ||v|| = sqrt(v1² + v2² + v3² + ...)

# Ví dụ hình học:
# v = [3, 4]  →  tam giác vuông cạnh 3 và 4, cạnh huyền = 5
# ||v|| = sqrt(3² + 4²) = sqrt(9 + 16) = sqrt(25) = 5

# Trong AI: dùng norm để chuẩn hóa vector trước khi so sánh độ tương đồng.

import numpy as np

v = np.array([3, 4])

# Cách 1: dùng numpy
norm = np.linalg.norm(v)
print(f"Độ dài vector: {norm}")  # 5.0

# Cách 2: tính tay
manual_norm = np.sqrt(sum(x ** 2 for x in v))
print(f"Tính tay: {manual_norm}")  # 5.0


# --- Tại sao cần độ dài vector? ---

# Dot product chỉ cho biết mức "trùng khớp" thô.
# Nếu không chia cho độ dài, vector lớn sẽ luôn có dot product lớn hơn
# dù hướng (nghĩa) có thể giống nhau.

# Ví dụ:
a = np.array([100, 200])   # cùng hướng, nhưng "lớn" gấp 100 lần
b = np.array([1, 2])       # cùng hướng, nhưng "nhỏ"

print(f"\nDot product a·b = {np.dot(a, b)}")  # 500 (lớn vì a lớn, không phải vì giống hơn)


# --- Cosine Similarity (Độ tương đồng cosin) ---

# Công thức đúng:
# similarity = dot_product / (||a|| × ||b||)

# Kết quả nằm trong [-1, 1]:
#   1  → cùng hướng (rất giống)
#   0  → vuông góc (không liên quan)
#  -1  → ngược hướng

# Ví dụ: so sánh 2 câu (vector đơn giản hóa theo từ)
# Từ vựng: [Tôi, thích, đọc, sách, báo]

# câu 1: "Tôi thích đọc sách"  →  [1, 1, 1, 1, 0]
# câu 2: "Tôi thích đọc báo"   →  [1, 1, 1, 0, 1]

cau1 = np.array([1, 1, 1, 1, 0])
cau2 = np.array([1, 1, 1, 0, 1])

dot = np.dot(cau1, cau2)                          # 1+1+1+0+0 = 3
norm1 = np.linalg.norm(cau1)                      # sqrt(4) = 2.0
norm2 = np.linalg.norm(cau2)                      # sqrt(4) = 2.0
similarity = dot / (norm1 * norm2)                # 3 / (2 × 2) = 0.75

# Ý nghĩa
# 3 = số từ trùng nhau giữa hai câu (Tôi, thích, đọc — 3 từ).

# Nhân ra 1 → cả hai câu đều có từ đó
# Nhân ra 0 → ít nhất một câu không có từ đó → không tính vào điểm trùng
# Hai câu có 4 từ giống nhau về mặt ngữ nghĩa, nhưng dot product chỉ đếm 3 vì "sách" và "báo" khác nhau và không cùng vị trí trong vector.


print(f"\nDot product: {dot}")
print(f"Độ dài câu 1: {norm1:.3f}")
print(f"Độ dài câu 2: {norm2:.3f}")
print(f"Cosine similarity: {similarity:.2f}")     # 0.75 → khá giống (4/5 từ trùng)

# Lưu ý: KHÔNG dùng len(vector) thay cho độ dài vector!
# len([1,1,1,1,0]) = 5  ← đây là SỐ PHẦN TỬ, không phải độ dài toán học
# np.linalg.norm([1,1,1,1,0]) = 2.0  ← mới là độ dài đúng


# Công thức:
# cos_sim = (a · b) / (||a|| * ||b||

# Kết quả từ -1 đến 1:

# 1: cùng hướng (giống nhau hoàn toàn)

# 0: không liên quan (vuông góc)

# -1: ngược hướng (đối nghịch)

# Ví dụ số:

# text
# a = [1, 2]
# b = [2, 4]

# Bước 1: dot product = 1*2 + 2*4 = 2 + 8 = 10
# Bước 2: ||a|| = sqrt(1+4) = sqrt(5) ≈ 2.236
# Bước 3: ||b|| = sqrt(4+16) = sqrt(20) ≈ 4.472
# Bước 4: cos_sim = 10 / (2.236 * 4.472) = 10 / 10 = 1.0

from sklearn.metrics.pairwise import cosine_similarity

a = np.array([[1, 2]])  # note: cần 2D array
b = np.array([[2, 4]])

cos_sim = cosine_similarity(a, b)
print(f"Cosine similarity: {cos_sim[0][0]}")  # 1.0

# Hoặc tự code:
def my_cosine_similarity(x, y):
    dot = np.dot(x, y)
    norm_x = np.linalg.norm(x)
    norm_y = np.linalg.norm(y)
    return dot / (norm_x * norm_y)

a_1d = np.array([1, 2])
b_1d = np.array([2, 4])
print(f"Self-implemented: {my_cosine_similarity(a_1d, b_1d)}")  # 1.0


# TÌM CÂU HỎI GIỐNG NHAU (search/chatbot)
question1 = "How to learn AI?"  # giả sử đã biến thành vector
question2 = "What is machine learning?"
question3 = "Cách học AI như thế nào?"

# Giả sử embeddings (vector) của 3 câu
q1_vec = np.array([0.8, 0.3, 0.5]) 
q2_vec = np.array([0.2, 0.7, 0.1])
q3_vec = np.array([0.75, 0.35, 0.55])

# Tính độ giống giữa q1 và các câu khác
sim_q1_q2 = cosine_similarity([q1_vec], [q2_vec])[0][0]
sim_q1_q3 = cosine_similarity([q1_vec], [q3_vec])[0][0]

print(f"Q1 vs Q2: {sim_q1_q2:.3f}")  # nhỏ hơn (không giống)
print(f"Q1 vs Q3: {sim_q1_q3:.3f}")  # lớn hơn (giống nhau)
# Kết quả: q3 giống q1 nhất → tìm ra câu hỏi tương tự!

# Đoạn code này làm gì?
# Đây là ví dụ tìm câu hỏi giống nhau trong chatbot/search — dùng cosine similarity trên embedding (vector số biểu diễn nghĩa câu).

# question1 = "How to learn AI?"           → q1_vec = [0.8, 0.3, 0.5]
# question2 = "What is machine learning?"  → q2_vec = [0.2, 0.7, 0.1]
# question3 = "Cách học AI như thế nào?"     → q3_vec = [0.75, 0.35, 0.55]
# Trong thực tế, model embedding (Word2Vec, BERT, …) biến câu thành vector. Ở đây vector được giả định sẵn để minh họa:

# Q1 và Q3 cùng nghĩa (“học AI thế nào”) → vector gần nhau
# Q1 và Q2 khác nghĩa → vector xa hơn

# Cách tính
# So sánh Q1 với Q2 và Q3 bằng công thức quen thuộc:

# cos_sim = dot / (||a|| × ||b||)
# cosine_similarity([q1_vec], [q2_vec])[0][0] — sklearn cần mảng 2D, nên bọc trong [...], kết quả lấy [0][0].

# Đáp án chi tiết
# Q1 vs Q2 — "How to learn AI?" vs "What is machine learning?"

# q1 = [0.8, 0.3, 0.5]
# q2 = [0.2, 0.7, 0.1]

# Bước 1 — Dot product:
#   0.8×0.2 + 0.3×0.7 + 0.5×0.1 = 0.16 + 0.21 + 0.05 = 0.42

# Bước 2 — ||q1||:
#   √(0.8² + 0.3² + 0.5²) = √(0.64 + 0.09 + 0.25) = √0.98 ≈ 0.990

# Bước 3 — ||q2||:
#   √(0.2² + 0.7² + 0.1²) = √(0.04 + 0.49 + 0.01) = √0.54 ≈ 0.735

# Bước 4 — Cosine similarity:
#   0.42 / (0.990 × 0.735) ≈ 0.577

# --> Q1 vs Q2: 0.577 — tương đối thấp, hai câu không giống nhau lắm.



# Q1 vs Q3 — "How to learn AI?" vs "Cách học AI như thế nào?"

# q1 = [0.8, 0.3, 0.5]
# q3 = [0.75, 0.35, 0.55]

# Bước 1 — Dot product:
#   0.8×0.75 + 0.3×0.35 + 0.5×0.55 = 0.60 + 0.105 + 0.275 = 0.98

# Bước 2 — ||q1|| ≈ 0.990  (như trên)

# Bước 3 — ||q3||:
#   √(0.75² + 0.35² + 0.55²) = √(0.5625 + 0.1225 + 0.3025) = √0.9875 ≈ 0.994

# Bước 4 — Cosine similarity:
#   0.98 / (0.990 × 0.994) ≈ 0.996

# Q1 vs Q3: 0.996 — rất cao, gần 1.0 → hai câu cùng nghĩa dù khác ngôn ngữ.



# Kết luận
# So sánh	Câu hỏi	Cosine sim	Ý nghĩa
# Q1 vs Q2
# "How to learn AI?" vs "What is machine learning?"
# 0.577
# Khác chủ đề
# Q1 vs Q3
# "How to learn AI?" vs "Cách học AI như thế nào?"
# 0.996
# Cùng nghĩa
# 0.996 > 0.577  →  Q3 giống Q1 nhất
# Ứng dụng thực tế: user hỏi Q1, hệ thống quét database, tính cosine similarity với mọi câu → trả về câu có điểm cao nhất (ở đây là Q3). Đó là cách semantic search và chatbot FAQ hoạt động ở mức cơ bản.

# Cần nhớ:

# Vector = mảng số

# Dot product = tổng tích từng cặp

# Cosine similarity = đo độ giống nhau, nằm trong [-1, 1]

# Trong AI: dùng để so sánh câu, ảnh, người dùng với nhau