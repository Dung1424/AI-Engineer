# Bài 03 Đọc CSV và ghi JSON

**Mục tiêu:** đọc một file thật, hiểu kiểu dữ liệu nhận được và tạo báo cáo có thể đọc lại.

## File và đường dẫn

CSV là bảng lưu bằng văn bản. Dòng đầu của bộ mẫu chứa tên cột. `csv.DictReader` dùng dòng đó làm khóa cho dict của từng bản ghi. Giá trị đọc được vẫn là chuỗi: điểm `8` trong file trở thành `"8"`, nên cần chuyển kiểu trước khi cộng.

`Path(__file__).resolve()` là đường dẫn tới file Python đang chạy. `parents[1]` trong ví dụ lấy thư mục chặng. Ghép `STAGE / "data" / "scores_clean.csv"` giúp tìm đúng file ngay cả khi chạy script từ một thư mục Terminal khác.

`with path.open(...) as stream` mở file rồi tự đóng khi ra khỏi khối. `newline=""` để module csv xử lý xuống dòng đúng cách; encoding `utf-8-sig` đọc được UTF-8 cả khi có BOM, thường gặp ở file xuất từ bảng tính.

JSON biểu diễn dữ liệu có cấu trúc. `json.dumps` đổi object Python thành chuỗi JSON; `json.loads` đọc lại chuỗi. `ensure_ascii=False` giữ chữ tiếng Việt dễ đọc. `None` của Python trở thành `null` trong JSON.

## Quan sát ví dụ

```bash
python 03-csv-and-json/example.py
```

Chương trình in kiểu score là `str`, đọc 5 bản ghi và tạo `outputs/lesson03/summary.json`. Mở file kết quả: nó có `row_count=5`, `first_score=8.0`. File dữ liệu gốc được giữ nguyên.

## Bài tự làm

Hoàn thành ba hàm trong `exercises.py`. Bài này chỉ dùng `scores_clean.csv`: chưa phải xử lý dữ liệu bẩn.

`read_csv(path)` trả danh sách dict; giữ điểm là chuỗi như lúc đọc. `build_report(records)` trả đúng hai khóa: `row_count` và `mean_score`. Với bộ sạch, kết quả là `5` và `7.0`; với danh sách rỗng, dùng `0` và `None`.

`write_json(path, report)` tạo thư mục cha khi thiếu, ghi UTF-8 và không thay đổi dict nhận vào. Thử ghi vào thư mục lồng nhau để chắc rằng code không chỉ chạy được khi thư mục đã tồn tại.

```bash
python check_exercises.py --lesson 03
```

Bạn đạt bài khi tự đọc được file JSON vừa ghi, kiểm tra con số từ CSV và giải thích được lỗi đường dẫn. Sau khi thử, xem [đáp án](solutions.py) nếu cần.

[Bài tiếp theo NumPy](../04-numpy/README.md)
