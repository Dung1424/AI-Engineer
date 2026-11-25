"""Biến, điều kiện và vòng lặp trên dữ liệu nhỏ."""

name = "An"
score = 8.0
passed = score >= 5
print(f"{name}: {score:.1f} điểm; đạt: {passed}")

scores = [8, 6, 10, 4, 7]
total = 0
passed_count = 0
for value in scores:
    total += value
    if value >= 5:
        passed_count += 1

print("Tổng:", total)
print("Trung bình:", total / len(scores))
print("Số người đạt:", passed_count)
