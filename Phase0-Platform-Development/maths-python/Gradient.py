# GRADIENT (Đạo hàm & Gradient Descent)
# Đạo hàm = độ dốc của đường cong

# Công thức trực quan:
# f'(x) = thay đổi của f(x) / thay đổi của x


# Ví dụ:

# hàm số: f(x) = x²
# đạo hàm: f'(x) = 2x
# gradient descent: x = x - learning_rate * f'(x)

# Ví dụ:

# f(x) = x² → f'(x) = 2x

# Tại x = 3: f'(3) = 6 (dốc lên)

# Tại x = -2: f'(-2) = -4 (dốc xuống)

# Code tính đạo hàm:
def derivative_at_point(f, x, h=0.0001):
    """Tính đạo hàm số gần đúng"""
    return (f(x + h) - f(x)) / h

# Ví dụ: f(x) = x²
f = lambda x: x**2

print(f"Đạo hàm tại x=3: {derivative_at_point(f, 3)}")  # xấp xỉ 6
print(f"Đạo hàm tại x=-2: {derivative_at_point(f, -2)}")  # xấp xỉ -4

# 2. Gradient với nhiều biến ⭐
# Gradient = vector chứa đạo hàm riêng theo từng biến.

# Ký hiệu: ∇f (đọc là "nabla f")

# Ví dụ 2 biến:

# text
# f(x, y) = x² + 2y²

# ∂f/∂x = 2x
# ∂f/∂y = 4y

# ∇f = [2x, 4y]

# Code tính gradient (PyTorch – quan trọng!):

import torch  # PyTorch có tính gradient tự động

# Định nghĩa hàm với 2 biến
x = torch.tensor(3.0, requires_grad=True)  # requires_grad để tính gradient
y = torch.tensor(2.0, requires_grad=True)

f = x**2 + 2*y**2

# Tính gradient tự động
f.backward()  # tính đạo hàm riêng theo x và y

print(f"∂f/∂x tại x=3, y=2: {x.grad}")  # 2*3 = 6
print(f"∂f/∂y tại x=3, y=2: {y.grad}")  # 4*2 = 8

# 3. Gradient Descent (CỰC KỲ QUAN TRỌNG) 

# Ý tưởng: Tìm điểm thấp nhất của hàm số bằng cách đi ngược hướng gradient.

# Công thức cập nhật:

# x_mới = x_cũ - learning_rate × gradient

# Ví dụ số: Tìm điểm thấp nhất của f(x) = x²

import numpy as np
import matplotlib.pyplot as plt

def gradient_descent_1d(start_x, learning_rate=0.1, steps=20):
    """Tìm min của f(x)=x² bằng gradient descent"""
    x = start_x
    history = [x]
    
    for step in range(steps):
        gradient = 2 * x  # đạo hàm của x²
        x = x - learning_rate * gradient
        history.append(x)
        print(f"Bước {step+1}: x = {x:.4f}, f(x) = {x**2:.4f}")
    
    return history

# Chạy thử từ x=10
history = gradient_descent_1d(start_x=10, learning_rate=0.1)

# Vẽ đường đi
# plt.plot(history, marker='o')
# plt.title('Gradient Descent cho f(x)=x²')
# plt.xlabel('Bước lặp')
# plt.ylabel('x')
# plt.show()

# Bước 1: x = 8.0000, f(x) = 64.0000
# Bước 2: x = 6.4000, f(x) = 40.9600
# Bước 3: x = 5.1200, f(x) = 26.2144
# Bước 4: x = 4.0960, f(x) = 16.7772
# Bước 5: x = 3.2768, f(x) = 10.7374
# ... về dần về 0

# Ví dụ thực tế: Tìm đường thẳng tốt nhất
# Bài toán: Cho 3 điểm (1,2), (2,3), (3,5). Tìm đường thẳng y = w×x + b gần các điểm nhất.

import numpy as np

# Dữ liệu
X = np.array([1, 2, 3])
y = np.array([2, 3, 5])

# Khởi tạo w, b ngẫu nhiên
w = 0.0
b = 0.0
learning_rate = 0.01

def loss(w, b):
    """Mean Squared Error: trung bình bình phương sai số"""
    y_pred = w * X + b
    return np.mean((y_pred - y)**2)

# Gradient descent cho w và b
for epoch in range(100):
    y_pred = w * X + b
    error = y_pred - y
    
    # Gradient (đạo hàm riêng)
    grad_w = 2 * np.mean(error * X)
    grad_b = 2 * np.mean(error)
    
    # Cập nhật
    w -= learning_rate * grad_w
    b -= learning_rate * grad_b
    
    if epoch % 20 == 0:
        print(f"Bước {epoch}: w={w:.3f}, b={b:.3f}, loss={loss(w,b):.3f}")

print(f"\nKết quả cuối: y = {w:.3f}x + {b:.3f}")
# Kết quả gần đúng: y = 1.5x + 0.5 (đường thẳng lý tưởng)

# Ứng dụng thực tế trong AI

# MÔ PHỎNG HỌC SÂU (Neural Network đơn giản nhất)
import torch
import torch.nn as nn

# Dữ liệu: dự đoán giá nhà từ diện tích
areas = torch.tensor([[50.0], [100.0], [150.0], [200.0]])  # m²
prices = torch.tensor([[300.0], [500.0], [700.0], [900.0]])  # triệu đồng

# Model: 1 lớp (y = w*x + b)
model = nn.Linear(1, 1)  # tự động tạo w và b
criterion = nn.MSELoss()  # hàm loss
optimizer = torch.optim.SGD(model.parameters(), lr=0.0001)

# Huấn luyện
for epoch in range(500):
    # Dự đoán
    predictions = model(areas)
    
    # Tính loss
    loss = criterion(predictions, prices)
    
    # Gradient descent (PyTorch tự động!)
    optimizer.zero_grad()  # xóa gradient cũ
    loss.backward()        # tính gradient
    optimizer.step()       # cập nhật w, b
    
    if epoch % 100 == 0:
        print(f"Bước {epoch}: loss = {loss.item():.4f}")

# Dự đoán giá cho nhà 120m²
new_area = torch.tensor([[120.0]])
predicted_price = model(new_area)
print(f"\nDự đoán giá nhà 120m²: {predicted_price.item():.0f} triệu")