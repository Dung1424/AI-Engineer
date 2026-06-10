# PROBABILITY (XÁC SUẤT CƠ BẢN)

# 1. Xác suất là gì?
# Xác suất = số đo khả năng xảy ra của một sự kiện, từ 0 (không bao giờ) đến 1 (chắc chắn).

# Xác suất = số lần xảy ra / số lần tổng cộng

# Ví dụ:

# Tung đồng xu:
# Xác suất mặt ngửa = 1/2
# Xác suất mặt sấp = 1/2

# Tung đồng xu 2 lần:
# Xác suất mặt ngửa lần 1 và mặt sấp lần 2 = 1/2 * 1/2 = 1/4

# Tung đồng xu 3 lần:
# Xác suất mặt ngửa lần 1 và mặt sấp lần 2 và mặt ngửa lần 3 = 1/2 * 1/2 * 1/2 = 1/8

# Tung đồng xu 4 lần:
# Xác suất mặt ngửa lần 1 và mặt sấp lần 2 và mặt ngửa lần 3 và mặt sấp lần 4 = 1/2 * 1/2 * 1/2 * 1/2 = 1/16

# Tung đồng xu 5 lần:
# Xác suất mặt ngửa lần 1 và mặt sấp lần 2 và mặt ngửa lần 3 và mặt sấp lần 4 và mặt ngửa lần 5 = 1/2 * 1/2 * 1/2 * 1/2 * 1/2 = 1/32

# Tung đồng xu 6 lần:
# Xác suất mặt ngửa lần 1 và mặt sấp lần 2 và mặt ngửa lần 3 và mặt sấp lần 4 và mặt ngửa lần 5 và mặt sấp lần 6 = 1/2 * 1/2 * 1/2 * 1/2 * 1/2 * 1/2 = 1/64

# Tung đồng xu 7 lần:
# Xác suất mặt ngửa lần 1 và mặt sấp lần 2 và mặt ngửa lần 3 và mặt sấp lần 4 và mặt ngửa lần 5 và mặt sấp lần 6 và mặt ngửa lần 7 = 1/2 * 1/2 * 1/2 * 1/2 * 1/2 * 1/2 * 1/2 = 1/128

# Tung đồng xu 8 lần:
# Xác suất mặt ngửa lần 1 và mặt sấp lần 2 và mặt ngửa lần 3 và mặt sấp lần 4 và mặt ngửa lần 5 và mặt sấp lần 6 và mặt ngửa lần 7 và mặt sấp lần 8 = 1/2 * 1/2 * 1/2 * 1/2 * 1/2 * 1/2 * 1/2 * 1/2 = 1/256

# Tung đồng xu 9 lần:
# Xác suất mặt ngửa lần 1 và mặt sấp lần 2 và mặt ngửa lần 3 và mặt sấp lần 4 và mặt ngửa lần 5 và mặt sấp lần 6 và mặt ngửa lần 7 và mặt sấp lần 8 và mặt ngửa lần 9 = 1/2 * 1/2 * 1/2 * 1/2 * 1/2 * 1/2 * 1/2 * 1/2 * 1/2 = 1/512

# Tung đồng xu 10 lần:
# Xác suất mặt ngửa lần 1 và mặt sấp lần 2 và mặt ngửa lần 3 và mặt sấp lần 4 và mặt ngửa lần 5 và mặt sấp lần 6 và mặt ngửa lần 7 và mặt sấp lần 8 và mặt ngửa lần 9 và mặt sấp lần 10 = 1/2 * 1/2 * 1/2 * 1/2 * 1/2 * 1/2 * 1/2 * 1/2 * 1/2 * 1/2 = 1/1024

import numpy as np
import random

# Mô phỏng tung đồng xu 1000 lần
coins = np.random.choice(['Ngửa', 'Sấp'], size=1000, p=[0.5, 0.5])
prob_ngua = np.sum(coins == 'Ngửa') / 1000
print(f"Xác suất ngửa (thực tế): {prob_ngua:.3f}")  # xấp xỉ 0.5

# Tung xúc sắc
dice = np.random.randint(1, 7, size=1000)
prob_6 = np.sum(dice == 6) / 1000
print(f"Xác suất ra 6: {prob_6:.3f}")

# 2. Phân phối xác suất (Distribution) 
# Phân phối xác suất = bảng tần suất của các giá trị có thể của một biến ngẫu nhiên.

# Phân phối rời rạc (Discrete)
# Chỉ có các giá trị cụ thể.

# Ví dụ: Tung xúc sắc

# P(X=1) = 1/6
# P(X=2) = 1/6
# P(X=3) = 1/6
# P(X=4) = 1/6
# P(X=5) = 1/6
# P(X=6) = 1/6

# Phân phối liên tục (Continuous)
# Có thể nhận bất kỳ giá trị nào trong khoảng.

# Quan trọng nhất: Phân phối chuẩn (Normal/Gaussian) – hình chuông

# Ví dụ: Chiều cao của người

# P(X=1.75) = 0
# P(X=1.76) = 0
# P(X=1.77) = 0
# P(X=1.78) = 0
# P(X=1.79) = 0
# P(X=1.80) = 0
# P(X=1.81) = 0
# P(X=1.82) = 0
# P(X=1.83) = 0
# P(X=1.84) = 0

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Phân phối chuẩn với mean=0, std=1
x = np.linspace(-4, 4, 100)
y = stats.norm.pdf(x, loc=0, scale=1)  # PDF = mật độ xác suất

# plt.plot(x, y)
# plt.title('Phân phối chuẩn (Standard Normal)')
# plt.xlabel('Giá trị')
# plt.ylabel('Mật độ')
# plt.grid(True)
# plt.show()

# Lấy mẫu từ phân phối chuẩn
samples = np.random.normal(loc=0, scale=1, size=1000)
print(f"Mean của mẫu: {np.mean(samples):.3f}")  # xấp xỉ 0
print(f"Std của mẫu: {np.std(samples):.3f}")   # xấp xỉ 1

# Tại sao quan trọng trong AI?

# Nhiều dữ liệu thực tế tuân theo phân phối chuẩn (chiều cao, điểm số, lỗi đo lường)

# Nhiều thuật toán giả định dữ liệu có phân phối chuẩn

3. Xác suất có điều kiện (Conditional Probability)
# Xác suất có điều kiện = xác suất của một sự kiện khi biết sự kiện khác đã xảy ra.

# Ví dụ:

# Xác suất để tung đồng xu mặt ngửa khi biết đã tung đồng xu mặt sấp = 1/2

# Xác suất để tung xúc sắc mặt 6 khi biết đã tung xúc sắc mặt 1 = 1/6

# Xác suất để tung xúc sắc mặt 6 khi biết đã tung xúc sắc mặt 1 = 1/6

# Xác suất để tung xúc sắc mặt 6 khi biết đã tung xúc sắc mặt 1 = 1/6

# Công thức vàng: P(A|B) = P(A và B) / P(B)

# Đọc là: "Xác suất của A biết B đã xảy ra"

# Ví dụ thực tế:

# A = trời mưa

# B = có mây

# P(mưa|có mây) = P(mưa và có mây) / P(có mây)

# Ví dụ số: Khảo sát 100 người
# 40 người thích coffee, 30 thích tea, 20 thích cả hai

total = 100
likes_coffee = 40
likes_tea = 30
likes_both = 20

# P(tea | coffee) = xác suất thích tea biết đã thích coffee
p_tea_given_coffee = likes_both / likes_coffee
print(f"P(tea | coffee) = {p_tea_given_coffee:.2f}")  # 20/40 = 0.5

# P(coffee | tea)
p_coffee_given_tea = likes_both / likes_tea
print(f"P(coffee | tea) = {p_coffee_given_tea:.2f}")  # 20/30 = 0.667

# 4. Công thức Bayes (SIÊU QUAN TRỌNG)
# Công thức Bayes = công thức xác suất có điều kiện.

# Ví dụ:

# P(A|B) = P(B|A) * P(A) / P(B)

# Ví dụ số: Khảo sát 100 người
# 40 người thích coffee, 30 thích tea, 20 thích cả hai

# P(tea | coffee) = P(coffee | tea) * P(tea) / P(coffee)

# Tại sao quan trọng? Cho phép đảo ngược xác suất có điều kiện.

# Ví dụ kinh điển: Chẩn đoán bệnh

# Giả sử có bệnh hiếm: 1% dân số mắc
# Xét nghiệm: 
# - Nếu có bệnh → dương tính 99% (độ nhạy)
# - Nếu không bệnh → dương tính 5% (dương tính giả)

# Hỏi: Nếu xét nghiệm dương tính, xác suất thực sự bị bệnh là bao nhiêu?

# Biết trước (prior)
p_benh = 0.01  # 1% dân số bị bệnh
p_khong_benh = 0.99

# Độ chính xác của xét nghiệm
p_duong_tinh_given_benh = 0.99   # nếu bị bệnh, 99% ra dương
p_duong_tinh_given_khong_benh = 0.05  # nếu khỏe, 5% vẫn ra dương

# Tính P(duong_tinh)
p_duong_tinh = (p_duong_tinh_given_benh * p_benh + 
                p_duong_tinh_given_khong_benh * p_khong_benh)

# Bayes: P(benh | duong_tinh)
p_benh_given_duong = (p_duong_tinh_given_benh * p_benh) / p_duong_tinh

print(f"Xác suất thực sự bị bệnh nếu xét nghiệm dương: {p_benh_given_duong:.2%}")
# Kết quả: khoảng 16.7% - rất thấp mặc dù xét nghiệm "chính xác 99%"!
# Giải thích: bệnh hiếm nên dương tính giả nhiều hơn dương tính thật

# 5. Ứng dụng trong AI: Spam Filter

# PHÂN LOẠI EMAIL SPAM DÙNG BAYES

# Dữ liệu giả: 100 email đã được gán nhãn
emails = [
    ("win money now", "spam"),
    ("meeting at 3pm", "not_spam"),
    ("free prize winner", "spam"),
    ("project deadline", "not_spam"),
    ("congratulations you won", "spam"),
]

# Tính xác suất prior
n_spam = sum(1 for _, label in emails if label == "spam")
p_spam = n_spam / len(emails)
p_not_spam = 1 - p_spam

# Hàm đơn giản hóa: tính xác suất từ xuất hiện trong spam/not_spam
def simple_bayes_spam_filter(email_text):
    # Thực tế phức tạp hơn nhiều, đây là demo
    spam_words = ["win", "money", "free", "prize", "congratulations", "winner"]
    
    # Đếm số từ spam trong email
    words = email_text.lower().split()
    spam_score = sum(1 for word in words if word in spam_words)
    
    # Quyết định dựa trên ngưỡng
    if spam_score >= 2:
        return "SPAM"
    else:
        return "NOT SPAM"

# Test
test_emails = [
    "win free money now",
    "meeting at 3pm tomorrow",
    "congratulations you won a free prize"
]

for email in test_emails:
    result = simple_bayes_spam_filter(email)
    print(f"'{email}' → {result}")

# 6. Sampling (Lấy mẫu)
# Tại sao cần? Không thể khảo sát toàn bộ dân số (quá lớn) → lấy mẫu đại diện.
# LẤY MẪU NGẪU NHIÊN

population = np.arange(1, 10001)  # 10,000 người
true_mean = np.mean(population)  # 5000.5

# Lấy mẫu ngẫu nhiên 100 người
sample = np.random.choice(population, size=100, replace=False)
sample_mean = np.mean(sample)

print(f"Mean thực tế: {true_mean:.1f}")
print(f"Mean từ mẫu: {sample_mean:.1f}")
print(f"Sai số: {abs(true_mean - sample_mean):.1f}")

# Mẫu càng lớn → càng chính xác
for size in [10, 50, 100, 500]:
    sample = np.random.choice(population, size=size, replace=False)
    print(f"Cỡ mẫu {size:3d}: mean = {np.mean(sample):.1f}")