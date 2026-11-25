# Chặng 1 Python và dữ liệu

**Đích đến:** tự viết chương trình nhận CSV, kiểm tra từng bản ghi, thống kê dữ liệu sạch và xuất kết quả. Đây là chặng tuần 1–4 trong bản Word đang học.

**Bắt đầu ở [00 Chuẩn bị](00-setup/README.md), sau đó học bài 01.** Chặng này làm bằng Python trên máy; không cần API key, GPU hoặc gọi model.

## Thứ tự học

| Tuần dự kiến | Bài | Làm xong khi |
| --- | --- | --- |
| Trước bài đầu | [00 Chuẩn bị](00-setup/README.md) | Tự chạy được file Python trong môi trường riêng. |
| 1 | [01 Python cơ bản](01-python-basics/README.md) | Dùng biến, điều kiện, vòng lặp để tính và đếm. |
| 1 | [02 Hàm và kiểm tra dữ liệu](02-functions-and-validation/README.md) | Chuyển kiểu, viết hàm, báo và xử lý lỗi đúng chỗ. |
| 1 | [03 CSV và JSON](03-csv-and-json/README.md) | Đọc file, hiểu kiểu dữ liệu, ghi báo cáo JSON. |
| 2 | [04 NumPy](04-numpy/README.md) | Hiểu shape, axis, mean, chuẩn hóa và phép `@`. |
| 3 | [05 pandas](05-pandas/README.md) | Lọc dữ liệu lỗi, xử lý trùng và thống kê theo nhóm. |
| 4 | [06 Dự án cuối chặng](06-csv-pipeline/README.md) | Chạy pipeline trên file mẫu và đầu vào lỗi, giải thích kết quả. |
| Mở rộng 1–2 tuần | [07 API CRUD và giao diện](07-crud-web-app/README.md) | Tự chạy ứng dụng web và theo dõi request qua schema, router, service, repository và database. |

Đây là lịch tham khảo khoảng 10–12 giờ/tuần. Nếu đã quen một phần từ web/backend, làm bài tập và tự kiểm tra trước để quyết định cần học lại bao nhiêu.

Bài 07 là project backend/web bổ sung ngoài lịch nền tảng bốn tuần. Project có môi trường riêng, ứng dụng hoàn chỉnh và bộ tests riêng; xem README trong project để chạy. `check_exercises.py --all` vẫn kiểm tra sáu bài tự làm 01–06, không thay cho tests của ứng dụng web.

## Cách học mỗi bài

Mở `README.md` để hiểu khái niệm và hợp đồng bài tập. Đoán đầu ra của `example.py`, chạy thử, rồi sửa một giá trị để quan sát. Sau đó tự viết trong `exercises.py`; các dòng `NotImplementedError` là phần cố ý để trống cho bạn làm.

Chạy bộ tự kiểm tra. Khi còn lỗi, đọc thông báo và thử lại trước khi mở `solutions.py`. Đáp án là một cách làm tham khảo, không phải code phải chép giống hệt. Bài dự án dùng `run.py` thay cho `example.py`.

Mọi lệnh bên dưới và trong các bài đều chạy từ thư mục `01-python-and-data`, với môi trường đã kích hoạt:

```bash
python 01-python-basics/example.py
python check_exercises.py --lesson 01
```

Kiểm tra tất cả bài tự làm khi kết thúc:

```bash
python check_exercises.py --all
```

Chỉ khi cần kiểm tra đáp án tham khảo, thêm `--source solutions`. Chạy đáp án vượt kiểm tra không có nghĩa bài của bạn đã hoàn thành. Bộ kiểm tra đánh giá hành vi trên các trường hợp mẫu; bạn vẫn cần giải thích code và tự thêm dữ liệu.

## Những thứ dùng chung

`data/` chứa dữ liệu gốc và đáp số của bộ mẫu. `outputs/` chỉ xuất hiện khi chạy bài ghi file; chương trình không sửa dữ liệu gốc. Ghi lại phần tự làm và câu còn vướng trong [PROGRESS.md](PROGRESS.md).

Nguồn chính thức để tra cứu: [Python Tutorial](https://docs.python.org/3/tutorial/), [csv](https://docs.python.org/3/library/csv.html), [NumPy basics](https://numpy.org/doc/stable/user/absolute_beginners.html), [pandas tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html). Đọc bài tiếng Việt trong repo trước, mở nguồn khi cần hiểu sâu một thao tác.
