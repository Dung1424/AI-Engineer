# Bài 02 Hàm và kiểm tra dữ liệu

**Mục tiêu:** tách một việc thành hàm và xử lý dữ liệu sai mà không dừng cả chương trình.

## Một bản ghi và nhiều bản ghi

`{"name": "An", "score": "8"}` là `dict`: các khóa gắn với giá trị. `record["score"]` lấy điểm của bản ghi. Một `list` có thể chứa nhiều dict, tương tự mảng các object bạn gặp khi xử lý JSON ở backend.

Một hàm có đầu vào, logic và giá trị trả về. Tách `parse_score(raw)` giúp viết quy tắc kiểm tra một lần rồi dùng cho mọi hàng. Hàm nên báo lỗi cụ thể khi đầu vào không đáp ứng hợp đồng.

Chuỗi `"8"` khác số `8`. `float("8")` tạo `8.0`, nhưng `float("abc")` gây `ValueError`. Cặp `try`/`except` cho phép xử lý lỗi rồi đi tiếp. Chỉ bắt lỗi bạn biết cách xử lý; không dùng một `except` bao trùm để bỏ qua mọi lỗi lập trình.

`NaN` nghĩa là giá trị không phải một số theo nghĩa tính toán thông thường; `inf` là vô cực. Chuyển sang float được chưa đủ: `math.isfinite(score)` kiểm tra giá trị hữu hạn, sau đó mới kiểm tra miền 0–10.

## Chạy ví dụ

```bash
python 02-functions-and-validation/example.py
```

An có điểm hợp lệ `8.0`; Bình bị loại vì `abc`. Sửa dữ liệu để thêm một người có `score="nan"`, rồi quan sát nhánh báo lỗi.

## Bài tự làm

Trong `exercises.py`, viết `parse_score(raw)` trả một float hữu hạn thuộc `[0, 10]`. Trường hợp thiếu/rỗng, sai kiểu, không phải số hoặc ngoài miền phải báo `ValueError`. Các đầu vào bài này là chuỗi, số hoặc `None`, không dùng giá trị boolean làm điểm.

Tiếp theo viết `separate_scores(values)`: gọi lại hàm trên, gom các điểm đúng theo thứ tự, đếm các giá trị sai, không sửa danh sách đầu vào.

| Lời gọi | Kết quả |
| --- | --- |
| `parse_score(" 7.5 ")` | `7.5` |
| `parse_score("abc")`, `parse_score("nan")`, `parse_score(12)` | Báo `ValueError`. |
| `separate_scores(["8", "", "abc", "11", "6"])` | `([8.0, 6.0], 3)` |
| `separate_scores([])` | `([], 0)` |

```bash
python check_exercises.py --lesson 02
```

Bạn đạt bài khi phân biệt được trả về một giá trị hợp lệ với báo một lỗi, và giải thích vì sao không nên âm thầm đổi điểm sai thành 0. Có thể đối chiếu [đáp án](solutions.py) sau khi thử.

[Bài tiếp theo CSV và JSON](../03-csv-and-json/README.md)
