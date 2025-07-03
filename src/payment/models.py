from enum import Enum
from datetime import datetime
from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import func, ForeignKey
from sqlalchemy import Enum as SQLAlchemyEnum

from src.database.models.base import Base

if TYPE_CHECKING:
    from src.order.models import Order


class PaymentMethod(str, Enum):
    CASH = "cash"
    CREDIT_CARD = "credit_card"
    SBP = "sbp"


class Payment(Base):
    total_price: Mapped[Decimal]
    created_at: Mapped[datetime] = mapped_column(func.now())
    is_paid: Mapped[bool] = mapped_column(default=False)
    payment_method: Mapped[PaymentMethod] = mapped_column(SQLAlchemyEnum(PaymentMethod))

    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"))
    order: Mapped["Order"] = relationship(back_populates="payment")
