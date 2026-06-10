# Gradient and Optimization for AI Engineer

Gradient là cơ chế giúp model học. Model dự đoán sai, loss tăng; gradient cho biết phải
điều chỉnh tham số theo hướng nào để loss giảm. Nếu probability là ngôn ngữ của sự không
chắc chắn, gradient là động cơ của quá trình training.

## 1. Mục Tiêu Học

Sau chương này, bạn cần hiểu được:

- Đạo hàm đo độ dốc của hàm số tại một điểm.
- Gradient là vector đạo hàm riêng khi hàm có nhiều biến.
- Loss function đo model sai bao nhiêu.
- Gradient descent cập nhật tham số để giảm loss.
- Learning rate ảnh hưởng đến tốc độ và độ ổn định của training.
- PyTorch autograd tính gradient tự động như thế nào.

## 2. Bức Tranh Lớn

Một model machine learning thường có tham số.

Ví dụ linear regression:

```text
y_pred = w*x + b
```

Trong đó:

```text
w, b = tham số model cần học
```

Quy trình học:

```text
1. Dự đoán y_pred
2. So sánh với y thật để tính loss
3. Tính gradient của loss theo tham số
4. Cập nhật tham số theo hướng làm loss giảm
5. Lặp lại nhiều lần
```

Đây là training loop cốt lõi của rất nhiều model.

## 3. Đạo Hàm

Đạo hàm đo độ dốc của hàm số.

```text
f'(x) = mức thay đổi của f(x) / mức thay đổi của x
```

Ví dụ:

```text
f(x) = x^2
f'(x) = 2x
```

Tại các điểm:

```text
x = 3  -> f'(3) = 6   -> dốc lên
x = -2 -> f'(-2) = -4 -> dốc xuống
x = 0  -> f'(0) = 0   -> đáy của hàm
```

Tính gần đúng bằng Python:

```python
def derivative_at_point(f, x, h=0.0001):
    return (f(x + h) - f(x)) / h

f = lambda x: x**2

print(derivative_at_point(f, 3))   # gần 6
print(derivative_at_point(f, -2))  # gần -4
```

Trực giác:

- Đạo hàm dương: đi sang phải thì hàm tăng.
- Đạo hàm âm: đi sang phải thì hàm giảm.
- Đạo hàm bằng 0: có thể là điểm thấp, điểm cao hoặc điểm phẳng.

## 4. Partial Derivative

Khi hàm có nhiều biến, ta cần đạo hàm riêng.

Ví dụ:

```text
f(x, y) = x^2 + 2y^2
```

Đạo hàm riêng theo `x`:

```text
df/dx = 2x
```

Đạo hàm riêng theo `y`:

```text
df/dy = 4y
```

Ý nghĩa:

- `df/dx` cho biết nếu chỉ thay đổi `x`, hàm thay đổi thế nào.
- `df/dy` cho biết nếu chỉ thay đổi `y`, hàm thay đổi thế nào.

## 5. Gradient

Gradient là vector gồm các đạo hàm riêng.

```text
gradient = [df/dx, df/dy]
```

Với:

```text
f(x, y) = x^2 + 2y^2
```

Ta có:

```text
gradient = [2x, 4y]
```

Tại `x = 3`, `y = 2`:

```text
gradient = [6, 8]
```

Python với PyTorch:

```python
import torch

x = torch.tensor(3.0, requires_grad=True)
y = torch.tensor(2.0, requires_grad=True)

f = x**2 + 2*y**2
f.backward()

print(x.grad)  # tensor(6.)
print(y.grad)  # tensor(8.)
```

Trong AI, tham số model có thể là hàng triệu hoặc hàng tỷ số. Gradient cho biết mỗi tham số
nên được sửa theo hướng nào.

## 6. Loss Function

Loss function đo model sai bao nhiêu.

Ví dụ regression:

```text
MSE = mean((y_pred - y_true)^2)
```

Ví dụ classification:

```text
Cross-entropy loss
```

Model training thực chất là bài toán:

```text
Tìm tham số làm loss nhỏ nhất.
```

## 7. Gradient Descent

Gradient descent là thuật toán đi ngược hướng gradient để giảm loss.

![Gradient descent](./images/gradient-descent.svg)

Công thức:

```text
parameter_new = parameter_old - learning_rate * gradient
```

Vì gradient chỉ hướng làm hàm tăng nhanh nhất, muốn giảm loss thì ta đi ngược hướng gradient.

Ví dụ với:

```text
f(x) = x^2
gradient = 2x
```

Python:

```python
def gradient_descent_1d(start_x, learning_rate=0.1, steps=10):
    x = start_x

    for step in range(steps):
        gradient = 2 * x
        x = x - learning_rate * gradient
        print(f"step={step+1}, x={x:.4f}, f(x)={x**2:.4f}")

gradient_descent_1d(start_x=10)
```

Trực giác:

- Bắt đầu ở `x = 10`, loss là `100`.
- Mỗi bước kéo `x` gần 0 hơn.
- Vì đáy của `x^2` nằm tại `x = 0`, loss giảm dần.

## 8. Learning Rate

Learning rate quyết định mỗi bước cập nhật lớn hay nhỏ.

```text
learning_rate quá nhỏ -> học rất chậm
learning_rate vừa đủ -> loss giảm ổn định
learning_rate quá lớn -> loss dao động hoặc tăng vọt
```

Ví dụ:

```python
for lr in [0.01, 0.1, 1.1]:
    print("learning_rate =", lr)
    gradient_descent_1d(start_x=10, learning_rate=lr, steps=5)
```

Khi train neural network, chọn learning rate là một trong những quyết định quan trọng nhất.

## 9. Batch, Epoch, Iteration

Ba khái niệm hay gặp:

```text
Batch     = một nhóm sample đưa vào model trong một lần cập nhật
Iteration = một lần cập nhật tham số
Epoch     = một lượt model đi qua toàn bộ training data
```

Ví dụ:

```text
Dataset có 1.000 sample
Batch size = 100
1 epoch = 10 iterations
```

Vì sao dùng batch:

- Train nhanh hơn so với từng sample.
- Đỡ tốn memory hơn so với dùng toàn bộ dataset.
- Gradient có nhiễu vừa phải, đôi khi giúp optimization tốt hơn.

## 10. Ví Dụ: Linear Regression Tự Viết

Bài toán:

```text
Cho các điểm (1, 2), (2, 3), (3, 5)
Tìm đường thẳng y = w*x + b gần các điểm nhất.
```

![Linear regression](./images/linear-regression.svg)

Code:

```python
import numpy as np

X = np.array([1, 2, 3])
y = np.array([2, 3, 5])

w = 0.0
b = 0.0
lr = 0.01

def mse_loss(w, b):
    y_pred = w * X + b
    return np.mean((y_pred - y) ** 2)

for epoch in range(200):
    y_pred = w * X + b
    error = y_pred - y

    grad_w = 2 * np.mean(error * X)
    grad_b = 2 * np.mean(error)

    w = w - lr * grad_w
    b = b - lr * grad_b

    if epoch % 50 == 0:
        print(epoch, w, b, mse_loss(w, b))

print("final:", w, b)
```

Điều đang xảy ra:

- `w` điều khiển độ dốc đường thẳng.
- `b` điều khiển vị trí đường thẳng.
- Gradient cho biết nên sửa `w` và `b` bao nhiêu để MSE giảm.

## 11. PyTorch Autograd

PyTorch tự động xây graph tính toán và tính gradient bằng `backward()`.

```python
import torch

x = torch.tensor(3.0, requires_grad=True)
y = x**2

y.backward()

print(x.grad)  # 6
```

Điều kiện để PyTorch tính gradient:

- Tensor phải có `requires_grad=True`.
- Kết quả phải phụ thuộc vào tensor đó.
- Gọi `.backward()` trên output scalar hoặc truyền gradient phù hợp.

## 12. PyTorch Training Loop

Ví dụ dự đoán giá nhà từ diện tích:

```python
import torch
import torch.nn as nn

areas = torch.tensor([[50.0], [100.0], [150.0], [200.0]])
prices = torch.tensor([[300.0], [500.0], [700.0], [900.0]])

model = nn.Linear(1, 1)
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.0001)

for epoch in range(500):
    predictions = model(areas)
    loss = criterion(predictions, prices)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

new_area = torch.tensor([[120.0]])
print(model(new_area))
```

Ba dòng quan trọng nhất:

```python
optimizer.zero_grad()  # xóa gradient cũ
loss.backward()        # tính gradient mới
optimizer.step()       # cập nhật tham số
```

Nếu quên `zero_grad()`, gradient sẽ bị cộng dồn qua nhiều bước và training có thể sai.

## 13. SGD, Mini-batch SGD Và Adam

Các optimizer thường gặp:

```text
Gradient Descent      -> dùng toàn bộ dataset để cập nhật
Stochastic GD         -> dùng 1 sample mỗi lần cập nhật
Mini-batch SGD        -> dùng một batch nhỏ
Adam                  -> optimizer phổ biến, tự điều chỉnh tốc độ theo từng tham số
```

Trong deep learning, Adam thường là lựa chọn mặc định tốt để bắt đầu.

## 14. Ứng Dụng Trong AI

Gradient xuất hiện trong:

- Linear regression.
- Logistic regression.
- Neural network.
- Backpropagation.
- Fine-tuning model.
- Training embedding.
- Reinforcement learning.

Hầu hết deep learning hiện đại đều dựa trên ý tưởng:

```text
Tính loss -> tính gradient -> cập nhật tham số.
```

## 15. Lỗi Hay Nhầm

- Nghĩ gradient là loss. Loss là mức sai; gradient là hướng sửa.
- Learning rate quá lớn làm loss tăng thay vì giảm.
- Quên `optimizer.zero_grad()` trong PyTorch.
- Gọi `.backward()` nhiều lần trên cùng graph mà không hiểu graph đã bị giải phóng.
- Dùng feature chưa scale làm gradient descent khó hội tụ.
- Nghĩ gradient descent luôn tìm được global minimum; với neural network, loss landscape phức tạp hơn.

## 16. Bài Tập

### Cơ bản

1. Với `f(x)=x^2`, tính đạo hàm tại `x=5`.
2. Với `f(x)=3x^2`, tính đạo hàm tại `x=2`.
3. Với `f(x,y)=x^2+y^2`, tính gradient tại `(3,4)`.

### Trung bình

1. Viết gradient descent để tìm min của `f(x)=(x-3)^2`.
2. Thử learning rate `0.01`, `0.1`, `1.0` và so sánh.
3. Tự viết linear regression bằng NumPy cho 5 điểm dữ liệu.

### AI-oriented

1. Giải thích training loop PyTorch bằng lời của bạn.
2. Giải thích vì sao cần `loss.backward()` trước `optimizer.step()`.
3. Giải thích vì sao feature scaling có thể giúp gradient descent ổn định hơn.

## 17. Checklist Cần Nhớ

- Đạo hàm đo độ dốc tại một điểm.
- Gradient là vector đạo hàm riêng.
- Loss đo model sai bao nhiêu.
- Gradient cho biết hướng sửa tham số.
- Gradient descent đi ngược hướng gradient để giảm loss.
- Learning rate quá nhỏ học chậm, quá lớn dễ mất ổn định.
- PyTorch dùng autograd để tính gradient tự động.

