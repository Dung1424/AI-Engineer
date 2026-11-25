# Bài 01 Python cơ bản

**Mục tiêu:** đọc được một chương trình ngắn, dùng điều kiện để ra quyết định và dùng vòng lặp để xử lý nhiều giá trị. Đây là phần ôn nhanh cho người đã từng lập trình web.

## Từ dữ liệu đến kết quả

Một biến là tên gắn với một giá trị. `name = "An"` là chuỗi (`str`), `count = 3` là số nguyên (`int`), `score = 8.0` là số thực (`float`). Biểu thức `score >= 5` tạo giá trị đúng/sai (`bool`). Dấu `=` gán giá trị, còn `==` so sánh bằng nhau.

```python
score = 8.0
if score >= 5:
    print("đạt")
else:
    print("chưa đạt")
```

Sau dấu `:` là một khối code được thụt vào. Python dùng thụt dòng để xác định khối, nên `print` ở trong `if` khác với `print` nằm ngoài. Dùng 4 dấu cách cho mỗi mức; đừng trộn tab và dấu cách.

Danh sách (`list`) như `[8, 6, 10, 4, 7]` chứa nhiều giá trị. `for score in scores` lấy từng giá trị ra. Biến đếm khởi tạo trước vòng lặp và tăng khi điều kiện đúng; nếu đặt nó bằng 0 bên trong vòng lặp, bạn sẽ xóa kết quả của các lượt trước.

## Chạy và quan sát

Từ thư mục chặng:

```bash
python 01-python-basics/example.py
```

Kết quả có tổng `35`, trung bình `7.0`, số người đạt `4`. Hãy đổi điểm 4 thành 5: tổng thành 36, trung bình 7.2, số người đạt thành 5. Đoán trước rồi mới chạy.

## Bài tự làm

Mở `exercises.py`, thay từng `raise NotImplementedError(...)` bằng code của bạn. `def` định nghĩa một hàm; `return` trả kết quả cho nơi gọi. Ví dụ `def gap_doi(x): return x * 2` nhận một số rồi trả số gấp đôi. Bài sau sẽ giải thích hàm kỹ hơn.

| Hàm | Đầu vào và đầu ra mẫu |
| --- | --- |
| `discounted_price(price, percent)` | `(100000, 20)` → `80000`; `(100, 0)` → `100`; `(100, 100)` → `0`. |
| `classify_score(score)` | `5` → `"đạt"`; `4.9` → `"chưa đạt"`. |
| `count_passed(scores)` | `[8, 6, 10, 4, 7]` → `4`; `[]` → `0`. |

Bài này giả định giá không âm, phần trăm từ 0 đến 100 và điểm từ 0 đến 10. Tập trung vào phép tính/điều kiện; kiểm tra đầu vào lỗi sẽ học ở bài 02. Trả kết quả bằng `return`, không chỉ `print`, để hàm được dùng tiếp trong chương trình.

```bash
python check_exercises.py --lesson 01
```

## Khi nào chuyển bài

Bạn cần giải thích được vì sao biến tổng/đếm nằm trước vòng lặp, phân biệt `print` với `return`, và xử lý được danh sách rỗng. Tự viết thêm một trường hợp kiểm tra cho mỗi hàm. Sau khi thử, có thể đối chiếu [đáp án](solutions.py).

[Bài tiếp theo Hàm và kiểm tra dữ liệu](../02-functions-and-validation/README.md)
