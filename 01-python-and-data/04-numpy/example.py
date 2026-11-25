import numpy as np

X = np.array([[1., 2.], [3., 4.]])
w = np.array([2., 1.])
print("Shape X:", X.shape)
print("Trung bình từng cột:", X.mean(axis=0).tolist())
print("Trung bình từng hàng:", X.mean(axis=1).tolist())
print("X @ w + 1:", (X @ w + 1).tolist())

mean = X.mean(axis=0)
std = X.std(axis=0)
safe_std = np.where(std == 0, 1., std)
Z = (X - mean) / safe_std
print("Chuẩn hóa:", Z.tolist())
print("Mẫu mới [5, 6]:", ((np.array([5., 6.]) - mean) / safe_std).tolist())
