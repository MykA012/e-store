from uuid import UUID
from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict

from src.order.models import PaymentMethod
from src.cart.schemas import ItemIDB


class OrderIDB(BaseModel):
    model_config=ConfigDict(from_attributes=True)

    id: int
    tracking_id: UUID
    total_price: Decimal
    payment_method: PaymentMethod
    is_paid: bool

    delivery_address: str
    delivery_date: datetime
    is_delivered: bool
    created_at: datetime
    user_id: int


class OrderWithItems(OrderIDB):
    model_config=ConfigDict(from_attributes=True)

    items: list[ItemIDB]
