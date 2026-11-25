import numpy as np


def column_statistics(X):
    """Nhận ma trận float hữu hạn không rỗng; trả (mean, std), dùng ddof=0."""
    raise NotImplementedError("TODO 1: tính theo axis=0")


def standardize(X, mean, std):
    """Dùng mean/std có sẵn; cột std=0 dùng mẫu số 1; không sửa đầu vào."""
    raise NotImplementedError("TODO 2: áp dụng z score")


def predict(X, w, b):
    """Các shape tương thích; trả ndarray của X @ w + b."""
    raise NotImplementedError("TODO 3: dùng @, không dùng vòng lặp")


if __name__ == "__main__":
    print("Hoàn thành ba hàm, rồi tự kiểm tra bài 04.")
