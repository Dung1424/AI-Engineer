import pytest
from sqlalchemy.exc import SQLAlchemyError

from app.repositories.product_repository import ProductRepository
from app.schemas.product import ProductCreate
from app.services.product_service import ProductService


def test_failed_commit_rolls_back_pending_changes(client, monkeypatch):
    with client.app.state.session_factory() as session:
        repository = ProductRepository(session)
        service = ProductService(repository)

        def fail_commit():
            raise SQLAlchemyError("Lỗi giả lập để kiểm tra transaction")

        monkeypatch.setattr(session, "commit", fail_commit)
        with pytest.raises(SQLAlchemyError):
            service.create_product(ProductCreate(name="Sản phẩm thử", price_vnd=1000))
        assert not session.new
        assert repository.count_products("") == 0
