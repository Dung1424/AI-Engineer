import csv
import json
from pathlib import Path


def read_csv(path):
    """Nhận Path/str, trả list[dict]; file ở bài này đúng cấu trúc bốn cột."""
    raise NotImplementedError("TODO 1: dùng with và csv.DictReader")


def build_report(records):
    """Dữ liệu sạch; trả row_count và mean_score; rỗng dùng None."""
    raise NotImplementedError("TODO 2: chuyển score sang float rồi tính")


def write_json(path, report):
    """Tạo thư mục cha khi thiếu, ghi UTF-8; không làm đổi report."""
    raise NotImplementedError("TODO 3: json.dumps với ensure_ascii=False")


if __name__ == "__main__":
    print("Hoàn thành ba hàm, rồi tự kiểm tra bài 03.")
