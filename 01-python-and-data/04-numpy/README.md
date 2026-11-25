# Bài 04 NumPy và dữ liệu dạng mảng

**Mục tiêu:** tính trên cả bảng bằng NumPy, hiểu hướng tính và kích thước kết quả. Chưa cần học hết đại số tuyến tính.

Nếu chưa cài thư viện, chạy `python -m pip install -r requirements.txt` từ thư mục chặng.

## Shape và axis bằng một bảng nhỏ

`X = np.array([[1., 2.], [3., 4.]])` là bảng 2 hàng và 2 cột, nên `X.shape` là `(2, 2)`. Trong ML thường quy ước hàng là mẫu, cột là đặc trưng. `w = [2., 1.]` có hai trọng số, tương ứng hai cột.

| Thao tác | Ý nghĩa trong bảng này | Kết quả |
| --- | --- | --- |
| `X.mean(axis=0)` | Gộp theo chiều các hàng, giữ một kết quả mỗi cột. | `[2., 3.]` |
| `X.mean(axis=1)` | Gộp theo chiều các cột, giữ một kết quả mỗi hàng. | `[1.5, 3.5]` |
| `X @ w + 1` | Tính tổng có trọng số rồi cộng độ lệch cho từng hàng. | `[5., 11.]` |

Khi thấy `@`, tính tay hàng đầu: `1×2 + 2×1 + 1 = 5`. Phép `X * w` là nhân từng phần tử có broadcasting, không thực hiện cùng phép cộng đó.

## Chuẩn hóa để làm gì

Chuẩn hóa z score lấy giá trị trừ trung bình rồi chia độ lệch chuẩn. Độ lệch chuẩn mô tả mức độ phân tán quanh trung bình; ở bài này dùng `std` mặc định của NumPy với `ddof=0`. Phần toán ở chặng 2 sẽ giải thích kỹ hơn.

Với bảng mẫu, mean là `[2, 3]`, std là `[1, 1]`, bảng chuẩn hóa là `[[-1, -1], [1, 1]]`. Một cột không đổi có std bằng 0; thay mẫu số đó bằng 1 để không chia cho 0. NumPy tự áp dụng vector thống kê cho từng hàng, gọi là broadcasting.

Mẫu mới `[5, 6]` phải dùng mean/std đã có, cho `[3, 3]`. Tính lại mean/std trên mỗi mẫu mới sẽ làm phép biến đổi không nhất quán. Khi làm ML, chỉ fit thống kê trên train rồi dùng chúng cho validation/test.

## Thực hành

```bash
python 04-numpy/example.py
```

Trong `exercises.py`, viết `column_statistics(X)`, `standardize(X, mean, std)` và `predict(X, w, b)` theo docstring. Đầu vào của bài là các mảng float hữu hạn, không rỗng, shape tương thích. Không sửa trực tiếp các mảng nhận vào.

```bash
python check_exercises.py --lesson 04
```

Bạn đạt bài khi tính tay được một hàng, giải thích shape đầu ra và xử lý một cột không đổi. Sau khi thử, xem [đáp án](solutions.py).

[Bài tiếp theo pandas](../05-pandas/README.md)
