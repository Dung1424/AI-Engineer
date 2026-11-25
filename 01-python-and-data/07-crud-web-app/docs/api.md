# Hợp đồng API

Base URL khi chạy tại máy: `http://127.0.0.1:8000/api/v1/products`.

| Method và đường dẫn | Công việc | Thành công |
| --- | --- | --- |
| `GET /api/v1/products` | Danh sách, tìm tên và phân trang. | 200 và object phân trang. |
| `POST /api/v1/products` | Tạo sản phẩm. | 201 và sản phẩm vừa tạo. |
| `GET /api/v1/products/{id}` | Xem một sản phẩm. | 200 và sản phẩm. |
| `PUT /api/v1/products/{id}` | Thay các trường sản phẩm. | 200 và sản phẩm sau thay đổi. |
| `DELETE /api/v1/products/{id}` | Xóa sản phẩm. | 204, body rỗng. |

## Dữ liệu vào

```json
{
  "name": "Sổ tay",
  "description": "Giấy kẻ ngang",
  "price_vnd": 35000,
  "stock": 12
}
```

Tên có 1–120 ký tự sau khi bỏ khoảng trắng đầu/cuối; mô tả tối đa 1000 ký tự. `price_vnd` là số nguyên từ 0 đến 1.000.000.000.000; `stock` là số nguyên từ 0 đến 1.000.000. Không gửi số dưới dạng chuỗi, giá thập phân hoặc boolean. `name` và `price_vnd` bắt buộc; `description` mặc định chuỗi rỗng và `stock` mặc định 0. Trường thừa, kể cả `id`, bị từ chối.

PUT ở project này là cập nhật cả bộ trường theo schema: nếu bỏ mô tả/tồn kho, hai trường đó về mặc định. Nó không có nghĩa cập nhật một vài trường như PATCH. Cả POST và PUT đều trả dữ liệu trên cùng, thêm `id` do database tạo.

## Danh sách và phân trang

GET hỗ trợ `q`, `page` và `page_size`. Mặc định page=1, page_size=5; page phải ≥1, page_size từ 1 đến 50, q tối đa 120 ký tự. Tìm kiếm chuỗi con trong tên, coi `%` và `_` là ký tự thường. SQLite không tự bảo đảm tìm kiếm không dấu hoặc chuyển hoa/thường cho mọi ký tự Unicode.

```bash
curl 'http://127.0.0.1:8000/api/v1/products?page=1&page_size=5'
```

Kết quả có `items`, `total`, `page`, `page_size`; `total` là số kết quả sau lọc, không chỉ số hàng trong trang hiện tại. Sản phẩm mới hơn đứng trước theo id giảm dần. Trang vượt số lượng hiện có trả danh sách rỗng; giao diện sẽ chuyển về trang cuối hợp lệ.

## Thử thêm bằng Terminal

Giữ server chạy, mở một Terminal khác:

```bash
curl -i 'http://127.0.0.1:8000/api/v1/products' \
  -H 'Content-Type: application/json' \
  -d '{"name":"Sổ tay","price_vnd":35000,"stock":12,"description":"Giấy kẻ ngang"}'
```

Đọc id từ kết quả rồi thử GET, PUT, DELETE với id đó. Có thể dùng Swagger `/docs` để nhập JSON mà không cần nhớ cú pháp curl.

## Đọc lỗi

422 nghĩa là dữ liệu hoặc tham số không đạt schema; phản hồi có `detail` và `errors`, mỗi lỗi có `field`, `message`. 404 nghĩa là không có sản phẩm mang id được yêu cầu. 503 là lỗi truy cập database đã được handler đổi thành thông báo chung; chi tiết kỹ thuật được ghi ở log server.

Không nhìn riêng HTTP 200 để kết luận nghiệp vụ đúng. Đối chiếu nội dung trả về với bản ghi, tải lại giao diện và kiểm tra dữ liệu còn sau khi khởi động lại.
