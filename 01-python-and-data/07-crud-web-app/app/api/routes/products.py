from fastapi import APIRouter, Depends, Path, Query, Response, status

from app.api.dependencies import get_product_service
from app.schemas.product import ProductCreate, ProductPage, ProductRead, ProductUpdate
from app.services.product_service import ProductService

router = APIRouter(prefix="/api/v1/products", tags=["Sản phẩm"])


@router.get("", response_model=ProductPage, summary="Lấy danh sách sản phẩm")
def list_products(
    q: str = Query(default="", max_length=120, description="Tìm theo tên"),
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=5, ge=1, le=50),
    service: ProductService = Depends(get_product_service),
):
    return service.list_products(q, page, page_size)


@router.post("", response_model=ProductRead, status_code=status.HTTP_201_CREATED,
             summary="Thêm sản phẩm")
def create_product(data: ProductCreate, service: ProductService = Depends(get_product_service)):
    return service.create_product(data)


@router.get("/{product_id}", response_model=ProductRead, summary="Xem một sản phẩm")
def get_product(product_id: int = Path(ge=1),
                service: ProductService = Depends(get_product_service)):
    return service.get_product(product_id)


@router.put("/{product_id}", response_model=ProductRead, summary="Thay nội dung sản phẩm")
def update_product(data: ProductUpdate, product_id: int = Path(ge=1),
                   service: ProductService = Depends(get_product_service)):
    return service.update_product(product_id, data)


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT,
               response_class=Response, summary="Xóa sản phẩm")
def delete_product(product_id: int = Path(ge=1),
                   service: ProductService = Depends(get_product_service)):
    service.delete_product(product_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
