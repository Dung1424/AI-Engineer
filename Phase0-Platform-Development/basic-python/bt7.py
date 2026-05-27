# Xử lý lỗi
try:
    number = int("abc")
    print(number)
except ValueError:
    print("Khong the chuyen thanh so")