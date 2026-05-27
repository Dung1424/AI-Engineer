class AppError(Exception):
    """Base exception cho business logic."""

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class BusinessError(AppError):
    """Lỗi nghiệp vụ — trả HTTP 400."""


class NotFoundError(AppError):
    """Resource không tồn tại — trả HTTP 404."""


class ForbiddenError(AppError):
    """Không có quyền — trả HTTP 403."""


class UnauthorizedError(AppError):
    """Chưa đăng nhập hoặc token không hợp lệ — trả HTTP 401."""
