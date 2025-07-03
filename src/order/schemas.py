from uuid import UUID, uuid4
from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel

from src.cart.schemas import ItemIDB


class OrderBase(BaseModel):
    delivery_address: str


class OrderIDB(OrderBase):
    id: int
    tracking_id: UUID
    total_price: Decimal
    delivery_date: datetime
    is_delivered: bool
    created_at: datetime
    user_id: int


class OrderWithItem(OrderIDB):
    items: list[ItemIDB]
