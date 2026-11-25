from pydantic import BaseModel, ConfigDict, Field


class ProductInput(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    name: str = Field(min_length=1, max_length=120, description="Tên sản phẩm")
    description: str = Field(default="", max_length=1000, description="Mô tả")
    price_vnd: int = Field(ge=0, le=1_000_000_000_000, strict=True, description="Giá nguyên đồng Việt Nam")
    stock: int = Field(default=0, ge=0, le=1_000_000, strict=True, description="Số lượng tồn kho")


class ProductCreate(ProductInput):
    pass


class ProductUpdate(ProductInput):
    """PUT thay toàn bộ các trường; giá trị không gửi dùng mặc định của schema."""


class ProductRead(ProductInput):
    model_config = ConfigDict(from_attributes=True)
    id: int


class ProductPage(BaseModel):
    items: list[ProductRead]
    total: int
    page: int
    page_size: int
