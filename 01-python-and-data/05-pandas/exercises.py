import pandas as pd


def clean_data(df):
    """Cột id/name/group đã đầy đủ; lọc score, rồi giữ mã hợp lệ đầu tiên.

    Trả DataFrame mới; không sửa df. score phải là kiểu số và thuộc [0, 10].
    """
    raise NotImplementedError("TODO 1: copy, to_numeric, lọc, drop_duplicates")


def mean_by_group(clean_df):
    """Nhận dữ liệu sạch; trả dict ánh xạ group sang điểm trung bình."""
    raise NotImplementedError("TODO 2: groupby rồi mean rồi to_dict")


if __name__ == "__main__":
    print("Hoàn thành hai hàm, rồi tự kiểm tra bài 05.")
