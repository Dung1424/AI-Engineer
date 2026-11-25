"""Tự hoàn thành pipeline. Hợp đồng chi tiết nằm trong README cùng thư mục."""

import csv
import json
import math
from pathlib import Path


def read_csv(path):
    """Trả list[dict] sau khi kiểm tra header và cấu trúc từng bản ghi."""
    raise NotImplementedError("TODO 1: đọc file UTF-8, kiểm tra bốn cột")


def clean_data(records):
    """Trả (valid, rejected); rejected có record_number, reason, data."""
    raise NotImplementedError("TODO 2: kiểm tra trường, điểm và mã trùng")


def summarize(records):
    """Trả valid_count, mean_score, passed_count, by_group."""
    raise NotImplementedError("TODO 3: thống kê; tập rỗng không chia cho 0")


def write_results(output_dir, valid, rejected, summary):
    """Ghi clean.csv, rejected.json và summary.json, có tổng số và số lỗi."""
    raise NotImplementedError("TODO 4: ghi kết quả, giữ nguyên dữ liệu gốc")


if __name__ == "__main__":
    print("Hoàn thành các hàm rồi chạy: python run.py")
