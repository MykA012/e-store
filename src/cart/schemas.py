from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class CartBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    items_count: int
    total_price: Decimal

    user_id: int
