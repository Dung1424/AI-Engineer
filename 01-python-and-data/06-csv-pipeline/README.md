# Bài 06 Dự án kiểm tra và thống kê CSV

**Sản phẩm:** một chương trình dòng lệnh đọc CSV, kiểm tra dữ liệu, ghi các dòng sạch, các dòng bị loại và báo cáo tổng hợp. Bài này nối kiến thức cả chặng; tính toán hoàn toàn bằng code, không gửi dữ liệu cho AI.

## Hợp đồng đầu vào

File UTF-8 có đúng bốn cột `id,name,group,score`; có thể đổi thứ tự cột nhưng không được thiếu, thừa hoặc lặp tên cột. CSV bị lỗi cấu trúc phải báo lỗi toàn file, không âm thầm bỏ qua.

Với từng bản ghi, bỏ khoảng trắng thừa đầu/cuối. Mã, tên và nhóm phải có nội dung; điểm phải chuyển sang số hữu hạn trong `[0, 10]`. Sau khi kiểm tra các trường, chỉ giữ hàng hợp lệ đầu tiên của mỗi mã. Điểm thiếu không được thay bằng 0 vì sẽ làm sai thống kê.

Quy tắc xuất hiện trước/sau áp dụng theo thứ tự bản ghi. Trường `record_number` trong log lỗi là số thứ tự bản ghi cộng 1 cho header; với bộ mẫu, nó trùng số dòng vật lý. File CSV có ô chứa nhiều dòng thì hai cách đếm không trùng nhau.

## Chia công việc thành bốn hàm

| Hàm trong `exercises.py` | Trách nhiệm |
| --- | --- |
| `read_csv(path)` | Kiểm tra header và số cột; trả danh sách dict chuỗi. |
| `clean_data(records)` | Trả `(valid, rejected)`; không sửa dữ liệu gốc. Điểm trong valid là float; rejected có `record_number`, `reason`, `data`. |
| `summarize(valid)` | Trả `valid_count`, `mean_score`, `passed_count`, `by_group`. Đạt nghĩa là điểm ≥ 5. Mỗi nhóm có `count`, `mean_score`. |
| `write_results(output_dir, valid, rejected, summary)` | Tạo thư mục và ba file kết quả. `summary.json` thêm `total_count`, `rejected_count`. |

Nếu không có bản ghi hợp lệ: số lượng và số đạt là 0, trung bình là `None` (JSON ghi `null`), thống kê nhóm là `{}`. Vẫn ghi được file sạch chỉ có header. Không chia cho 0.

## Chạy bản tự làm

Sau khi hoàn thành các TODO, chạy từ thư mục chặng:

```bash
python 06-csv-pipeline/run.py
python check_exercises.py --lesson 06
```

`run.py` đã lo nhận tham số và báo lỗi; bạn tập trung vào bốn hàm xử lý. Ban đầu nó báo `CHƯA XONG` vì phần tự làm còn trống. Tên và cách diễn đạt lý do lỗi do bạn chọn; lý do phải không rỗng và giúp hiểu lỗi.

Nếu cần chạy đáp án để đối chiếu sau khi thử:

```bash
python 06-csv-pipeline/run.py --source solutions
```

Kết quả mẫu là `Tổng: 9 | Hợp lệ: 5 | Bị loại: 4`, điểm trung bình `7.0`. Trong `outputs/csv-pipeline/` có `clean.csv`, `rejected.json`, `summary.json`. Log lỗi chứa các bản ghi tương ứng dòng 6, 7, 8, 9. Nhóm A có 2 người và B có 3 người; cả hai trung bình 7.0.

Tự tính lại tổng 35 và số đạt 4 để đối chiếu. Đừng chỉ nhìn việc chương trình không bị lỗi.

## Kiểm tra thêm trước khi hoàn thành

Thử file chỉ có header, file không tồn tại, thiếu cột, sai số cột trong hàng, điểm `nan`/`inf` và mã lặp. Thử một mã xuất hiện sai trước rồi đúng sau. Chạy lại hai lần và so nội dung ba file; không đưa thời gian hiện tại vào báo cáo này để việc đối chiếu được rõ.

```bash
python 06-csv-pipeline/run.py --input data/scores_clean.csv --output outputs/clean-pipeline
```

Đường dẫn `--input` và `--output` tương đối tính từ thư mục Terminal hiện tại; đường dẫn mặc định tính theo vị trí script. Không đặt đầu vào trùng một file đầu ra. Chạy lại cùng thư mục output sẽ ghi lại ba file báo cáo.

Bạn hoàn thành chặng khi tự viết được các hàm, đọc được log, giải thích được dữ liệu bị loại và chứng minh thống kê không dùng dòng sai. Lúc đó mới chuyển sang [Chặng 2 Toán phục vụ AI](../../02-math-for-ai/README.md).
