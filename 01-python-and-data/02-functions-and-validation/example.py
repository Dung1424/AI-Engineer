"""List chứa nhiều bản ghi; dict biểu diễn một bản ghi; hàm xử lý một việc."""

import math


def parse_score(raw):
    try:
        score = float(raw)
    except (TypeError, ValueError) as exc:
        raise ValueError("Điểm phải là một số") from exc
    if not math.isfinite(score) or not 0 <= score <= 10:
        raise ValueError("Điểm phải hữu hạn và thuộc [0, 10]")
    return score


if __name__ == "__main__":
    records = [{"name": "An", "score": "8"},
               {"name": "Bình", "score": "abc"}]
    for record in records:
        try:
            score = parse_score(record["score"])
        except ValueError as exc:
            print(record["name"], "bị loại:", exc)
        else:
            print(record["name"], "hợp lệ:", score)
