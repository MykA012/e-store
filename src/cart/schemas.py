from decimal import Decimal

from pydantic import BaseModel, ConfigDict

from src.product.schemas import ProductIDB


class Item(BaseModel):
    quantity: int
    product: ProductIDB


class CartIDB(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    items_count: int
    total_price: Decimal
    items: list[Item]
