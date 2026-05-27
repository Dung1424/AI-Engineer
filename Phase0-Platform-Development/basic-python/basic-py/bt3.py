# List dùng để lưu nhiều giá trị.

scores = [8, 9, 7, 10]

print(scores[0])      # 8
print(len(scores))    # 4

# Thêm phần tử vào cuối list
scores.append(6)
print(scores)

# Thêm phần tử vào vị trí cụ thể
scores.insert(1, 8.5)
print(scores)

# Xóa phần tử theo vị trí
scores.pop(2)
print(scores)

# Xóa phần tử theo giá trị
scores.remove(8.5)
print(scores)

# Sắp xếp list
scores.sort()
print(scores)

# Đảo ngược list
scores.reverse()
print(scores)