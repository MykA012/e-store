from decimal import Decimal

from pydantic import BaseModel, ConfigDict

from src.product.schemas import ProductIDB


class Item(BaseModel):
    quantity: int
    product: ProductIDB


class CartBase(BaseModel):
    items_count: int
    total_price: Decimal


class CartIDB(CartBase):
    model_config = ConfigDict(from_attributes=True)
    items: list[Item]
