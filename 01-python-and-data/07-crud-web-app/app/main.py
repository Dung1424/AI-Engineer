from contextlib import asynccontextmanager
from typing import Optional

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.exc import SQLAlchemyError

from app.api.routes.products import router as products_router
from app.core.config import PROJECT_ROOT, Settings
from app.core.errors import ProductNotFoundError
from app.core.handlers import database_error_handler, product_not_found_handler, validation_error_handler
from app.db.base import Base
from app.db.session import create_session_factory
from app.models.product import Product  # Đăng ký model trong Base.metadata.


def create_app(settings: Optional[Settings] = None) -> FastAPI:
    settings = settings or Settings()
    engine, session_factory = create_session_factory(settings.database_url)

    @asynccontextmanager
    async def lifespan(application: FastAPI):
        # Bài nhập môn tự tạo bảng còn thiếu; thay đổi schema cần migration.
        Base.metadata.create_all(engine)
        try:
            yield
        finally:
            engine.dispose()

    application = FastAPI(title=settings.app_name, version="1.0.0", lifespan=lifespan)
    application.state.session_factory = session_factory
    application.add_exception_handler(ProductNotFoundError, product_not_found_handler)
    application.add_exception_handler(RequestValidationError, validation_error_handler)
    application.add_exception_handler(SQLAlchemyError, database_error_handler)
    application.include_router(products_router)
    application.mount("/static", StaticFiles(directory=PROJECT_ROOT / "frontend"), name="static")

    @application.get("/", include_in_schema=False)
    def index():
        return FileResponse(PROJECT_ROOT / "frontend" / "index.html")

    return application


app = create_app()
