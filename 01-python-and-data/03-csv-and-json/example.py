"""Đọc file theo vị trí chương trình, không phụ thuộc thư mục Terminal."""

import csv
import json
from pathlib import Path

STAGE = Path(__file__).resolve().parents[1]


def main():
    source = STAGE / "data" / "scores_clean.csv"
    with source.open(encoding="utf-8-sig", newline="") as stream:
        records = list(csv.DictReader(stream))
    print("Bản ghi đầu:", records[0])
    print("Kiểu score sau đọc CSV:", type(records[0]["score"]).__name__)

    report = {"row_count": len(records), "first_score": float(records[0]["score"])}
    destination = STAGE / "outputs" / "lesson03" / "summary.json"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n",
                           encoding="utf-8")
    print("Đã ghi:", destination)
    print("Nội dung:", json.loads(destination.read_text(encoding="utf-8")))


if __name__ == "__main__":
    main()
