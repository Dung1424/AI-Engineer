"""Chạy bài tự làm hoặc đáp án; mặc định chạy bài tự làm."""

import argparse
import csv
import importlib
from pathlib import Path

STAGE = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description="Đọc, kiểm tra và thống kê CSV")
    parser.add_argument("--source", choices=["exercises", "solutions"], default="exercises")
    parser.add_argument("--input", type=Path, default=STAGE / "data" / "scores_raw.csv")
    parser.add_argument("--output", type=Path, default=STAGE / "outputs" / "csv-pipeline")
    args = parser.parse_args()
    input_path, output_path = args.input.resolve(), args.output.resolve()
    if input_path in [output_path / name for name in
                      ("clean.csv", "summary.json", "rejected.json")]:
        parser.error("Đường dẫn kết quả không được ghi đè file đầu vào")
    implementation = importlib.import_module(args.source)
    try:
        records = implementation.read_csv(input_path)
        valid, rejected = implementation.clean_data(records)
        summary = implementation.summarize(valid)
        implementation.write_results(output_path, valid, rejected, summary)
    except NotImplementedError as exc:
        print("CHƯA XONG:", exc)
        return 1
    except (OSError, ValueError, csv.Error, UnicodeError) as exc:
        print("KHÔNG XỬ LÝ ĐƯỢC:", exc)
        return 1
    print(f"Tổng: {len(records)} | Hợp lệ: {len(valid)} | Bị loại: {len(rejected)}")
    print("Điểm trung bình:", summary["mean_score"])
    print("Kết quả:", output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
