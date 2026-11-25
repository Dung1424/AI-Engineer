# Bài 07 Ứng dụng CRUD với API và giao diện

**Sản phẩm của bài học:** ứng dụng quản lý sản phẩm chạy trên máy, có thêm, xem, sửa, xóa, tìm theo tên và phân trang. Dữ liệu được lưu trong SQLite; giao diện gọi API thật bằng `fetch`.

Đây là project độc lập nằm trong repo học tập, có dependency, cấu hình, frontend, backend và tests riêng. Có thể tách nguyên thư mục này thành một repository sau. Bài học dùng kiến trúc phân lớp phù hợp với CRUD nhỏ; cách tổ chức này là một phương án tham chiếu, không phải kiến trúc duy nhất cho mọi dự án.

## Chạy lần đầu trên Mac

Các lệnh sau chạy từ thư mục project này, khác với thư mục chặng của các bài 01–06:

```bash
cd /Users/dangtiendung/Downloads/AI-Engineer/01-python-and-data/07-crud-web-app
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
cp .env.example .env
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Mở **http://127.0.0.1:8000** để dùng giao diện. Mở **http://127.0.0.1:8000/docs** để xem và thử từng API. Không mở `frontend/index.html` bằng cách nhấp đúp: frontend cần được phục vụ từ cùng ứng dụng Python để gọi đúng API.

`.venv/` chứa Python và thư viện của project; `.env` chứa cấu hình được `Settings` đọc. Lần sau chỉ cần vào thư mục, kích hoạt `.venv` và chạy Uvicorn. `Ctrl+C` dừng server.

Lần khởi động đầu tự tạo bảng còn thiếu trong `data/products.db`; cơ sở dữ liệu ban đầu rỗng. Hãy tự thêm một sản phẩm qua form. Tải lại trang hoặc dừng/chạy lại server vẫn giữ dữ liệu. Ví dụ SQLite ở đây đủ cho bài học; tạo bảng bằng `create_all` không thay thế migration khi bạn sửa schema.

## Kiến trúc và thứ tự đọc code

| Đường dẫn | Trách nhiệm |
| --- | --- |
| `frontend/index.html`, `styles.css` | Cấu trúc và giao diện. |
| `frontend/app.js` | Nhận tương tác, quản lý trạng thái và hiển thị dữ liệu. |
| `frontend/api.js` | Gửi HTTP request, đọc JSON và xử lý lỗi API. |
| `app/api/routes/products.py` | HTTP endpoint, status code, gọi service. |
| `app/schemas/product.py` | Kiểm tra body và mô tả response bằng Pydantic. |
| `app/services/product_service.py` | Điều phối use case, kiểm tra tồn tại và commit/rollback. |
| `app/repositories/product_repository.py` | Truy vấn và thay đổi dữ liệu qua SQLAlchemy. |
| `app/models/product.py` | Định nghĩa bảng và các trường lưu trong database. |
| `app/db/` | Engine, session và lớp cơ sở ORM. |
| `app/api/dependencies.py` | Cấp session riêng cho request và ghép repository/service. |
| `app/core/` | Đọc cấu hình và đổi lỗi thành phản hồi phù hợp. |
| `app/main.py` | Khởi tạo ứng dụng, đăng ký router, phục vụ frontend. |
| `tests/` | Kiểm tra CRUD và transaction bằng database tạm. |

Đọc [Giải thích kiến trúc](docs/architecture.md), sau đó theo một thao tác thêm sản phẩm từ `app.js` xuống repository rồi trở lại giao diện. Không cần hiểu toàn bộ code trước khi chạy thử.

## Một vòng CRUD để kiểm chứng

Thêm “Sổ tay” với giá 35000, tồn kho 12. Sản phẩm phải xuất hiện trong bảng. Bấm Sửa để nạp lại thông tin từ API, đổi giá thành 45000 rồi lưu. Tải lại trang: giá mới phải còn. Bấm Xóa và xác nhận: sản phẩm biến mất; API GET theo mã cũ trả 404.

Các trường code/JSON dùng tiếng Anh: `id`, `name`, `description`, `price_vnd`, `stock`. Giá là số nguyên đồng Việt Nam, không dùng float để biểu diễn tiền trong bài này. Hướng dẫn, nhãn form và thông báo ứng dụng bằng tiếng Việt.

## Chạy kiểm thử

Từ thư mục project, với môi trường đã kích hoạt:

```bash
python -m pytest -q
```

Tests dùng database riêng trong thư mục tạm, không ghi vào dữ liệu bạn đang thao tác. Các trường hợp gồm CRUD, giá/tồn kho đầu vào sai, sản phẩm không tồn tại, phân trang, tìm kiếm, dữ liệu giữ được khi khởi động lại và rollback khi commit thất bại.

## Học tiếp trong project

[Hợp đồng API và ví dụ gọi](docs/api.md) giúp thử endpoint trước khi đọc frontend. [Bài thực hành theo lớp](docs/practice.md) hướng dẫn quan sát request và tự thêm chức năng. Bài này là phần mở rộng thực hành web/backend của chặng Python; dự kiến dành thêm 1–2 tuần nếu API và ORM còn mới.

Frontend hiện dùng HTML/CSS/JavaScript thuần, không cần Node hay build. API và giao diện chạy cùng origin. Khi đã hiểu luồng, có thể thay frontend bằng Vue mà vẫn dùng cùng hợp đồng API. Project này tập trung vào CRUD; đăng nhập/phân quyền, migration và triển khai sẽ được học ở các phần mở rộng.

[Quay lại chặng 1](../README.md)
