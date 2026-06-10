# STATISTICS (THỐNG KÊ CƠ BẢN)

# 1. Mean (Trung bình)
# Mean = tổng của tất cả các giá trị / số lượng giá trị.
# Công thức: mean = (x1 + x2 + x3 + ... + xn) / n
# Ví dụ:

# x1 = 1, x2 = 2, x3 = 3, x4 = 4, x5 = 5
# mean = (1 + 2 + 3 + 4 + 5) / 5 = 3

import numpy as np
import pandas as pd

scores = [7, 8, 9, 6, 10]

# Các cách tính mean
print(f"Mean: {np.mean(scores)}")           # 8.0
print(f"Mean (manual): {sum(scores)/len(scores)}")  # 8.0

# Với pandas
df = pd.DataFrame({'scores': scores})
print(f"Pandas mean: {df['scores'].mean()}")  # 8.0

# 2. Median (Trung vị)
# Median = giá trị ở giữa sau khi sắp xếp tăng dần.
# Công thức: median = (n + 1) / 2

scores = [7, 8, 9, 6, 10]

# Các cách tính median
print(f"Median: {np.median(scores)}")           # 8.0
print(f"Median (manual): {sorted(scores)[len(scores)//2]}")  # 8.0

# Với pandas
df = pd.DataFrame({'scores': scores})
print(f"Pandas median: {df['scores'].median()}")  # 8.0

# Trong AI: Mean dùng để chuẩn hóa dữ liệu (trừ mean đi để dữ liệu có trung bình = 0)
# Trong AI: Median dùng để tìm giá trị trung vị của dữ liệu (giá trị ở giữa sau khi sắp xếp tăng dần)

# 2. Variance (Phương sai) - Đo độ phân tán 
# Variance = trung bình của bình phương các độ lệch so với trung bình.
# Công thức: variance = (x1 - mean)² + (x2 - mean)² + ... + (xn - mean)² / n
# Ví dụ:

# Scores: [7, 8, 9, 6, 10]
# Mean = 8

# Tính từng bước:
# (7-8)² = 1
# (8-8)² = 0
# (9-8)² = 1
# (6-8)² = 4
# (10-8)² = 4
# Tổng = 1+0+1+4+4 = 10
# Variance = 10/5 = 2

# Standard Deviation (độ lệch chuẩn) = √2 ≈ 1.414

# Trong AI: Variance dùng để đo độ phân tán của dữ liệu (độ lệch so với trung bình)
# Trong AI: Variance dùng để tìm giá trị trung vị của dữ liệu (giá trị ở giữa sau khi sắp xếp tăng dần)

scores = [7, 8, 9, 6, 10]

variance = np.var(scores)  # variance
std = np.std(scores)       # standard deviation

print(f"Variance: {variance:.2f}")  # 2.00
print(f"Std: {std:.2f}")            # 1.41

# So sánh 2 tập dữ liệu
data1 = [5, 5, 5, 5, 5]  # không phân tán
data2 = [1, 3, 5, 7, 9]  # phân tán nhiều

print(f"Data1 variance: {np.var(data1)}")  # 0
print(f"Data2 variance: {np.var(data2)}")  # 8

# Trong AI:

# Variance cao → dữ liệu đa dạng

# Dùng trong PCA (tìm chiều có variance cao nhất)

# 3. Correlation (Tương quan)

# Đo mức độ quan hệ tuyến tính giữa 2 biến, từ -1 đến 1:

# r ≈ 1: tương quan dương mạnh (x tăng → y tăng)

# r ≈ 0: không tương quan tuyến tính

# r ≈ -1: tương quan âm mạnh (x tăng → y giảm)

# ví dụ số 
# Dữ liệu: số giờ học và điểm thi
hours = [1, 2, 3, 4, 5]
scores = [50, 55, 65, 70, 80]

correlation = np.corrcoef(hours, scores)[0, 1]
print(f"Hệ số tương quan: {correlation:.3f}")  # ≈ 0.989 (rất mạnh)

# Ví dụ không tương quan
height = [150, 160, 170, 180, 190]
iq = [100, 105, 98, 110, 102]  # không liên quan chiều cao

corr_height_iq = np.corrcoef(height, iq)[0, 1]
print(f"Tương quan chiều cao vs IQ: {corr_height_iq:.3f}")  # gần 0

# Trực quan hóa:

import matplotlib.pyplot as plt

# Tạo 3 loại tương quan
np.random.seed(42)
x = np.linspace(0, 10, 50)

# Tương quan dương
y_pos = 2*x + np.random.normal(0, 2, 50)

# Tương quan âm
y_neg = -2*x + np.random.normal(0, 2, 50)

# Không tương quan
y_none = np.random.normal(5, 3, 50)

# Vẽ (bỏ comment để chạy)
# fig, axes = plt.subplots(1, 3, figsize=(12, 4))
# axes[0].scatter(x, y_pos)
# axes[0].set_title(f'Positive correlation: r={np.corrcoef(x,y_pos)[0,1]:.2f}')
# axes[1].scatter(x, y_neg)
# axes[1].set_title(f'Negative correlation: r={np.corrcoef(x,y_neg)[0,1]:.2f}')
# axes[2].scatter(x, y_none)
# axes[2].set_title(f'No correlation: r={np.corrcoef(x,y_none)[0,1]:.2f}')
# plt.show()

# Trong AI:

# Phát hiện feature có liên quan đến target

# Loại bỏ feature tương quan quá cao (tránh đa cộng tuyến)

# 4. Ứng dụng thực tế: Phân tích dữ liệu nhà đất
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Tạo dữ liệu nhà đất giả
np.random.seed(42)
n_houses = 100

data = {
    'area': np.random.normal(100, 30, n_houses),  # diện tích m²
    'bedrooms': np.random.randint(1, 5, n_houses),
    'age': np.random.randint(0, 30, n_houses),
    'price': np.random.normal(500, 150, n_houses)
}

# Thêm mối quan hệ: giá tăng theo diện tích
data['price'] = data['price'] + data['area'] * 3

df = pd.DataFrame(data)

# 1. Thống kê cơ bản
print("=== THỐNG KÊ CƠ BẢN ===")
print(f"Mean area: {df['area'].mean():.1f} m²")
print(f"Std area: {df['area'].std():.1f}")
print(f"Mean price: {df['price'].mean():.1f} triệu")
print(f"Std price: {df['price'].std():.1f}")

# 2. Ma trận tương quan
print("\n=== MA TRẬN TƯƠNG QUAN ===")
correlation_matrix = df.corr()
print(correlation_matrix['price'].sort_values(ascending=False))

# 3. Trực quan hóa
# fig, axes = plt.subplots(1, 2, figsize=(10, 4))
# axes[0].scatter(df['area'], df['price'])
# axes[0].set_xlabel('Area (m²)')
# axes[0].set_ylabel('Price (triệu)')
# axes[0].set_title(f'Correlation: {df["area"].corr(df["price"]):.2f}')
# 
# axes[1].scatter(df['age'], df['price'])
# axes[1].set_xlabel('Age (years)')
# axes[1].set_ylabel('Price (triệu)')
# axes[1].set_title(f'Correlation: {df["age"].corr(df["price"]):.2f}')
# plt.tight_layout()
# plt.show()

# 5. Sampling (Lấy mẫu) trong thực tế
# SO SÁNH CỠ MẪU KHÁC NHAU

population = np.random.normal(100, 15, 100000)  # 100,000 người
true_mean = np.mean(population)

# Thử nghiệm với các cỡ mẫu khác nhau
sample_sizes = [10, 30, 100, 300, 1000]
errors = []

for size in sample_sizes:
    # Lấy mẫu ngẫu nhiên 100 lần
    sample_errors = []
    for _ in range(100):
        sample = np.random.choice(population, size=size)
        sample_mean = np.mean(sample)
        sample_errors.append(abs(true_mean - sample_mean))
    
    avg_error = np.mean(sample_errors)
    errors.append(avg_error)
    print(f"Cỡ mẫu {size:4d}: sai số TB = {avg_error:.3f}")

# Kết luật: mẫu càng lớn, sai số càng nhỏ (Luật số lớn)

# Trong AI:

# Khi train model, không cần dùng hết dữ liệu nếu dữ liệu quá lớn

# Lấy mẫu để đánh giá model nhanh

