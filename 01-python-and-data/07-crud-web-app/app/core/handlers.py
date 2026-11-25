import logging

from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError

from app.core.errors import ProductNotFoundError

logger = logging.getLogger(__name__)


async def product_not_found_handler(request: Request, exc: ProductNotFoundError):
    return JSONResponse(status_code=404, content={"detail": str(exc)})


async def validation_error_handler(request: Request, exc: RequestValidationError):
    messages = {
        "missing": "Trường này là bắt buộc.",
        "string_too_short": "Nội dung không được để trống.",
        "string_too_long": "Nội dung vượt số ký tự cho phép.",
        "string_type": "Giá trị phải là chuỗi ký tự.",
        "int_type": "Giá trị phải là số nguyên.",
        "int_parsing": "Giá trị phải là số nguyên.",
        "greater_than_equal": "Giá trị nhỏ hơn mức tối thiểu.",
        "less_than_equal": "Giá trị vượt mức tối đa.",
        "extra_forbidden": "Trường này không được phép gửi lên.",
        "json_invalid": "Nội dung gửi lên không phải JSON hợp lệ.",
    }
    errors = [
        {"field": ".".join(str(part) for part in error["loc"][1:]),
         "message": messages.get(error["type"], "Giá trị không hợp lệ.")}
        for error in exc.errors()
    ]
    return JSONResponse(status_code=422, content={"detail": "Dữ liệu không hợp lệ.", "errors": errors})


async def database_error_handler(request: Request, exc: SQLAlchemyError):
    logger.error("Không thể hoàn tất thao tác với cơ sở dữ liệu.", exc_info=exc)
    return JSONResponse(status_code=503, content={"detail": "Không thể truy cập dữ liệu. Vui lòng thử lại."})
