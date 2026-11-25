from typing import Optional

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models.product import Product


class ProductRepository:
    def __init__(self, session: Session):
        self.session = session

    def list_products(self, query: str, offset: int, limit: int) -> list[Product]:
        statement = select(Product)
        if query:
            statement = statement.where(Product.name.contains(query, autoescape=True))
        statement = statement.order_by(Product.id.desc()).offset(offset).limit(limit)
        return list(self.session.scalars(statement))

    def count_products(self, query: str) -> int:
        statement = select(func.count(Product.id))
        if query:
            statement = statement.where(Product.name.contains(query, autoescape=True))
        return self.session.scalar(statement) or 0

    def get_product(self, product_id: int) -> Optional[Product]:
        return self.session.get(Product, product_id)

    def add_product(self, values: dict) -> Product:
        product = Product(**values)
        self.session.add(product)
        return product

    def update_product(self, product: Product, values: dict) -> Product:
        for field, value in values.items():
            setattr(product, field, value)
        return product

    def delete_product(self, product: Product) -> None:
        self.session.delete(product)
