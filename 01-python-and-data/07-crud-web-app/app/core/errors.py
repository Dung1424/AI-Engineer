class ProductNotFoundError(Exception):
    def __init__(self, product_id: int):
        self.product_id = product_id
        super().__init__(f"Không tìm thấy sản phẩm #{product_id}.")
