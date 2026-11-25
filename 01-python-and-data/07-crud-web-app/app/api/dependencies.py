from typing import Generator

from fastapi import Depends, Request
from sqlalchemy.orm import Session

from app.repositories.product_repository import ProductRepository
from app.services.product_service import ProductService


def get_session(request: Request) -> Generator[Session, None, None]:
    # Mỗi request dùng một session riêng, đóng khi hoàn tất request.
    with request.app.state.session_factory() as session:
        yield session


def get_product_service(session: Session = Depends(get_session)) -> ProductService:
    return ProductService(ProductRepository(session))
