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