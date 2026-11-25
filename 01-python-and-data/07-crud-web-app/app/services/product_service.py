from sqlalchemy.exc import SQLAlchemyError

from app.core.errors import ProductNotFoundError
from app.models.product import Product
from app.repositories.product_repository import ProductRepository
from app.schemas.product import ProductCreate, ProductUpdate


class ProductService:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def list_products(self, query: str, page: int, page_size: int) -> dict:
        query = query.strip()
        return {
            "items": self.repository.list_products(query, (page - 1) * page_size, page_size),
            "total": self.repository.count_products(query),
            "page": page,
            "page_size": page_size,
        }

    def get_product(self, product_id: int) -> Product:
        product = self.repository.get_product(product_id)
        if product is None:
            raise ProductNotFoundError(product_id)
        return product

    def create_product(self, data: ProductCreate) -> Product:
        product = self.repository.add_product(data.model_dump())
        self._commit()
        self.repository.session.refresh(product)
        return product

    def update_product(self, product_id: int, data: ProductUpdate) -> Product:
        product = self.get_product(product_id)
        self.repository.update_product(product, data.model_dump())
        self._commit()
        self.repository.session.refresh(product)
        return product

    def delete_product(self, product_id: int) -> None:
        product = self.get_product(product_id)
        self.repository.delete_product(product)
        self._commit()

    def _commit(self) -> None:
        try:
            self.repository.session.commit()
        except SQLAlchemyError:
            self.repository.session.rollback()
            raise
