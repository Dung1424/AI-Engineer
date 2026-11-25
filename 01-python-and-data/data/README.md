# Dữ liệu mẫu của chặng 1

Đây là dữ liệu tự tạo để học, không phải thông tin của người thật.

Mỗi hàng biểu diễn một học viên. `id` là mã, `name` là tên, `group` là nhóm, `score` là điểm từ 0 đến 10. Một mã hợp lệ chỉ được xuất hiện một lần trong kết quả sạch.

`scores_clean.csv` có 5 học viên hợp lệ. Tổng điểm 35, trung bình 7.0; 4 người đạt từ 5 điểm. Nhóm A có 2 người, nhóm B có 3 người; trung bình của cả hai nhóm là 7.0.

`scores_raw.csv` có 9 bản ghi: 5 hợp lệ và 4 cần loại. Dòng tiêu đề tính là dòng 1.

| Dòng trong file mẫu | Lỗi |
| --- | --- |
| 6 | S05 thiếu điểm. |
| 7 | S06 có điểm `abc`, không chuyển thành số được. |
| 8 | S07 có điểm 12, vượt giới hạn. |
| 9 | S01 đã xuất hiện hợp lệ ở dòng 2. |

Trong bài cuối chặng, kiểm tra mã/tên/nhóm, điểm, rồi mới kiểm tra trùng mã. Chỉ ghi nhận mã vào tập đã gặp sau khi cả hàng hợp lệ; nếu lần xuất hiện đầu sai nhưng lần sau đúng, giữ lần đúng. Nếu hai hàng cùng mã đều đúng, giữ hàng đầu.

Không sửa file gốc để làm cho bài tập vượt kiểm tra. Có thể sao chép ra file khác để thử dữ liệu mới.
