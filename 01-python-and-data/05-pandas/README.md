# Bài 05 Làm sạch và nhóm dữ liệu với pandas

**Mục tiêu:** nhìn một bảng dữ liệu, phát hiện dòng lỗi và thống kê phần hợp lệ. NumPy phù hợp với mảng số; pandas bổ sung bảng có tên cột (`DataFrame`) và cột dữ liệu (`Series`).

## Đọc và lọc

Ví dụ đọc `scores_raw.csv` với `dtype=str, keep_default_na=False` để chủ động nhận chuỗi thô, kể cả ô rỗng. `pd.to_numeric(..., errors="coerce")` đổi điểm sang số; chuỗi không đổi được thành giá trị thiếu. Tùy chọn này không tự nói được nguyên nhân lỗi, nên dự án cuối sẽ ghi riêng lý do.

`df["score"].between(0, 10)` tạo một cột True/False cho điều kiện. `df.loc[mask]` lấy các hàng đúng. `.copy()` tạo bản làm việc riêng, giúp hàm không thay đổi bảng gốc của người gọi.

Sau khi lọc điểm, `drop_duplicates(subset="id", keep="first")` giữ hàng hợp lệ đầu tiên của mỗi mã. Thứ tự này quan trọng: nếu hàng đầu của một mã sai, bạn vẫn muốn giữ hàng sau có điểm hợp lệ.

## Thống kê theo nhóm

`df.groupby("group")["score"].mean()` chia dữ liệu theo group rồi tính trung bình từng nhóm. Đây là phép tính trên dữ liệu, chưa phải model học quy luật. `to_dict()` chuyển kết quả thành dict để dùng trong code khác.

```bash
python 05-pandas/example.py
```

Kết quả: 9 dòng đầu vào; 2 điểm thiếu/không chuyển được; sau loại điểm ngoài miền và trùng mã còn 5 dòng. Trung bình 7.0; hai nhóm A và B đều trung bình 7.0. Không nhầm “2 ô thiếu/sai kiểu” với “4 dòng bị loại” vì còn hai loại lỗi khác.

## Bài tự làm

Trong `exercises.py`, viết `clean_data(df)` trả DataFrame mới có score là số trong `[0, 10]`, không trùng id và không làm đổi bảng gốc. Bài này giả định id/name/group đã đầy đủ; dự án cuối chặng mới kiểm tra các trường đó.

Viết `mean_by_group(clean_df)` trả `{"A": 7.0, "B": 7.0}` cho bộ mẫu. Nếu không còn hàng hợp lệ thì hàm trả dict rỗng.

```bash
python check_exercises.py --lesson 05
```

Bạn đạt bài khi giải thích được thứ tự lọc rồi loại trùng, và cho thấy bảng đầu vào chưa bị sửa. Đối chiếu [đáp án](solutions.py) sau khi thử.

[Bài tiếp theo Dự án cuối chặng](../06-csv-pipeline/README.md)
