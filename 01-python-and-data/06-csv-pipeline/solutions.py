"""Pipeline tham khảo cho file nhỏ; không cần pandas hoặc model AI."""

import csv
import json
import math
from pathlib import Path

COLUMNS = ["id", "name", "group", "score"]


def read_csv(path):
    with Path(path).open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream, strict=True)
        headers = reader.fieldnames
        if headers is None or len(headers) != 4 or set(headers) != set(COLUMNS):
            raise ValueError("Header phải có đúng id,name,group,score")
        rows = list(reader)
    if any(None in row or any(value is None for value in row.values()) for row in rows):
        raise ValueError("Có bản ghi thừa hoặc thiếu cột")
    return rows


def clean_data(records):
    valid, rejected, seen = [], [], set()
    for row_number, record in enumerate(records, start=2):
        try:
            item = {key: str(record[key]).strip() for key in COLUMNS}
            if not all(item[key] for key in ("id", "name", "group")):
                raise ValueError("Thiếu mã, tên hoặc nhóm")
            try:
                score = float(item["score"])
            except (TypeError, ValueError) as exc:
                raise ValueError("Điểm bị thiếu hoặc không phải số") from exc
            if not math.isfinite(score) or not 0 <= score <= 10:
                raise ValueError("Điểm phải hữu hạn và thuộc [0, 10]")
            if item["id"] in seen:
                raise ValueError("Trùng mã học viên đã hợp lệ")
        except (KeyError, TypeError, ValueError) as exc:
            rejected.append({"record_number": row_number, "reason": str(exc),
                             "data": record.copy()})
        else:
            item["score"] = score
            valid.append(item)
            seen.add(item["id"])
    return valid, rejected


def summarize(records):
    scores = [row["score"] for row in records]
    groups = {}
    for row in records:
        groups.setdefault(row["group"], []).append(row["score"])
    return {
        "valid_count": len(scores),
        "mean_score": sum(scores) / len(scores) if scores else None,
        "passed_count": sum(score >= 5 for score in scores),
        "by_group": {name: {"count": len(values),
                             "mean_score": sum(values) / len(values)}
                       for name, values in sorted(groups.items())},
    }


def write_results(output_dir, valid, rejected, summary):
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    with (output / "clean.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(valid)
    report = dict(summary, total_count=len(valid) + len(rejected),
                  rejected_count=len(rejected))
    for filename, value in (("summary.json", report), ("rejected.json", rejected)):
        (output / filename).write_text(
            json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n",
            encoding="utf-8")
