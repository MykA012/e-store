from decimal import Decimal

from pydantic import BaseModel, ConfigDict


# Cart
class CartBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    items_count: int
    total_price: Decimal

    user_id: int


class ItemCreate(CartBase):
    pass


class CartIDB(CartBase):
    id: int


# Item
class ItemBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    quantity: int

    cart_id: int
    product_id: int


class ItemCreate(ItemBase):
    pass


class ItemIDB(ItemBase):
    id: int
