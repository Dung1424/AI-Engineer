"""Đáp án tham khảo; chỉ mở sau khi tự làm bài tập."""


def discounted_price(price, percent):
    return price * (1 - percent / 100)


def classify_score(score):
    if score >= 5:
        return "đạt"
    return "chưa đạt"


def count_passed(scores):
    count = 0
    for score in scores:
        if score >= 5:
            count += 1
    return count
