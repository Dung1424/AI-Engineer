# Học project qua một yêu cầu thật

Mở project chạy được trước, rồi thực hiện các bài dưới. Bạn có thể sửa trực tiếp code; project này là ví dụ hoàn chỉnh để nghiên cứu, khác với các file TODO ở bài 01–06.

## Buổi 1 Quan sát HTTP và JSON

Mở Developer Tools của trình duyệt, chọn Network. Thêm một sản phẩm, đọc method, URL, request body, status và response. So giá trị của `price_vnd` trong JSON với cách giao diện hiển thị dấu phân tách tiền. Dữ liệu trao đổi vẫn là số, phần định dạng nằm ở frontend.

Thử gửi một request qua Swagger hoặc curl với giá âm, tên chỉ chứa dấu cách, giá dạng chuỗi và một trường không tồn tại. Ghi lại 422, trường lỗi và thông báo. Bài đạt khi bạn phân biệt kiểm tra ở trình duyệt với kiểm tra ở server.

## Buổi 2 Theo luồng từng lớp

Đặt breakpoint hoặc thêm log ngắn ở route create, `ProductService.create_product` và `ProductRepository.add_product`. Thêm một sản phẩm rồi quan sát thứ tự. Phân biệt đối tượng `ProductCreate` đã qua schema với ORM `Product` và JSON response.

Giải thích bằng lời tại sao repository chưa commit ngay sau `add_product`. Tìm nơi đóng session và nơi đổi lỗi sản phẩm không tồn tại thành 404. Chạy tests để đối chiếu sau khi bỏ các log thử nghiệm.

## Buổi 3 Tự thêm một quy tắc nghiệp vụ

Thêm quy tắc: chỉ xóa sản phẩm có tồn kho bằng 0. Tạo lỗi nghiệp vụ riêng trong `app/core/errors.py`, kiểm tra tại service, thêm handler trả 409, và dùng cơ chế thông báo sẵn có của frontend để hiển thị lỗi.

Viết hai test: xóa sản phẩm còn hàng phải bị từ chối và bản ghi vẫn còn; xóa sản phẩm hết hàng phải thành công. Đây là lúc service có thêm logic thay vì chỉ chuyển dữ liệu qua repository. Không đặt riêng quy tắc ở nút Xóa vì người khác vẫn gọi API trực tiếp được.

## Buổi 4 Thêm một tính năng từ giao diện tới database

Thêm bộ lọc chỉ hiện sản phẩm còn hàng. Frontend gửi một query parameter có tên tiếng Anh; route kiểm tra kiểu, service nhận điều kiện, repository áp dụng cùng điều kiện cho cả list và count. Kiểm tra tổng số kết quả, các trang và trường hợp không còn kết quả.

Bài đạt khi bạn chỉ đúng mỗi file đã đổi và trách nhiệm của thay đổi đó. Nếu thay cấu trúc bảng, học thêm migration trước khi áp dụng lên database có dữ liệu muốn giữ.

## Tự tổng kết

Viết lại luồng thêm sản phẩm bằng lời của bạn, kể tên các lớp đã đi qua và dạng dữ liệu ở từng điểm. Sau đó đổi một thông báo hoặc thêm một trường giới hạn mới trong schema, chạy lại tests và quan sát frontend. Giữ tên file/biến/hàm bằng tiếng Anh; phần giải thích và thông báo bằng tiếng Việt.
