"""Chỉ kiểm tra và báo thông tin; không tự cài thư viện hoặc đổi cấu hình."""

import importlib
import platform
import sys


def main():
    print("Python:", platform.python_version())
    print("Đường dẫn:", sys.executable)
    print("Môi trường riêng:", "Có" if sys.prefix != sys.base_prefix else "Chưa")
    print("Bài 01–03 và dự án CSV chỉ cần thư viện có sẵn của Python.")
    for name in ("numpy", "pandas"):
        try:
            package = importlib.import_module(name)
        except ImportError:
            print(name + ": chưa cài; chỉ cần khi tới bài 04–05.")
        else:
            print(name + ": " + package.__version__)


if __name__ == "__main__":
    main()
