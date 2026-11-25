import math


def parse_score(raw):
    try:
        score = float(raw)
    except (TypeError, ValueError) as exc:
        raise ValueError("Điểm không phải số") from exc
    if not math.isfinite(score) or not 0 <= score <= 10:
        raise ValueError("Điểm ngoài miền hợp lệ")
    return score


def separate_scores(values):
    valid, error_count = [], 0
    for value in values:
        try:
            valid.append(parse_score(value))
        except ValueError:
            error_count += 1
    return valid, error_count
