import numpy as np

X = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 3.0, 5.0])

w = 0.0
b = 0.0
learning_rate = 0.1
epochs = 20

def mse(y_pred, y_true):
    return np.mean((y_pred - y_true) ** 2)

print("epoch |    w    |    b    |  loss  | grad_w | grad_b")
print("-" * 58)

for epoch in range(epochs + 1):
    y_pred = w * X + b
    error = y_pred - y
    loss = mse(y_pred, y)

    grad_w = 2 * np.mean(error * X)
    grad_b = 2 * np.mean(error)

    print(
        f"{epoch:5d} | {w:7.3f} | {b:7.3f} | "
        f"{loss:6.3f} | {grad_w:6.3f} | {grad_b:6.3f}"
    )

    w = w - learning_rate * grad_w
    b = b - learning_rate * grad_b