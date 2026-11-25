import math


def parse_score(raw):
    """Trả float hữu hạn thuộc [0, 10]; dữ liệu không hợp lệ báo ValueError."""
    raise NotImplementedError("TODO 1: chuyển kiểu và kiểm tra điểm")


def separate_scores(values):
    """Trả (valid_scores, error_count); giữ thứ tự; không sửa values."""
    raise NotImplementedError("TODO 2: tái sử dụng parse_score")


if __name__ == "__main__":
    print("Hoàn thành parse_score và separate_scores, rồi tự kiểm tra bài 02.")
