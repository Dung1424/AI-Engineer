# Bài 00 Chuẩn bị để học

Mục tiêu của bài này là tự chạy được một file Python và biết chương trình đang dùng môi trường nào. Chưa cần cài toàn bộ công cụ AI.

## Python và môi trường riêng là gì

Python là chương trình đọc và chạy file `.py` của bạn. Terminal là nơi nhập lệnh như `python example.py`; file `.py` chứa code Python như `print("Xin chào")`. Hai loại lệnh đó được viết ở hai nơi khác nhau.

`venv` tạo một môi trường chứa các gói dành riêng cho chặng học. Khi kích hoạt nó, lệnh `python` và `python -m pip` cùng trỏ về môi trường đó. `pip` cài thư viện; viết `python -m pip` giúp gắn đúng pip với Python đang chạy.

## Thực hiện trên Mac

Mở Terminal và chạy lần lượt:

```bash
cd /Users/dangtiendung/Downloads/AI-Engineer/01-python-and-data
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python 00-setup/check_environment.py
```

Các bài được viết để chạy với Python 3.9 trở lên. Kết quả cần thấy: phiên bản Python, đường dẫn chứa `.venv`, dòng `Môi trường riêng: Có`. NumPy và pandas có thể báo chưa cài; ba bài đầu vẫn chạy bằng thư viện có sẵn.

Mỗi lần mở Terminal mới, vào thư mục chặng rồi kích hoạt lại:

```bash
cd /Users/dangtiendung/Downloads/AI-Engineer/01-python-and-data
source .venv/bin/activate
```

Khi đến NumPy và pandas, cài các thư viện bằng:

```bash
python -m pip install -r requirements.txt
```

Chương trình kiểm tra môi trường chỉ báo thông tin; không tự cài gói hay đổi cấu hình máy.

## Tự xác nhận

Tạo một file `hello.py` trong thư mục này, viết `print("Bắt đầu học Python")`, rồi từ thư mục chặng chạy `python 00-setup/hello.py`. Bạn đạt bài khi tự làm được việc đó và chỉ đúng vị trí file.

Nếu gặp `can't open file`, kiểm tra vị trí bằng `pwd` và tên file bằng `ls`. Nếu gặp `ModuleNotFoundError`, xem đã kích hoạt đúng môi trường và cài đúng gói chưa. Chép cả lệnh vừa chạy lẫn thông báo lỗi khi cần mình hỗ trợ.

[Học tiếp bài 01](../01-python-basics/README.md)
