from enum import Enum
from uuid import UUID, uuid4
from datetime import datetime
from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import func, ForeignKey
from sqlalchemy import Enum as SQLAlchemyEnum

from src.database.models.base import Base

if TYPE_CHECKING:
    from src.cart.models import Item
    from src.user.models import User


class PaymentMethod(str, Enum):
    CASH = "cash"
    CREDIT_CARD = "credit_card"
    SBP = "sbp"


class Order(Base):
    tracking_id: Mapped[UUID] = mapped_column(default=uuid4, index=True, unique=True)
    total_price: Mapped[Decimal] = mapped_column(default=Decimal("0"))
    payment_method: Mapped[PaymentMethod] = mapped_column(SQLAlchemyEnum(PaymentMethod))
    is_paid: Mapped[bool] = mapped_column(default=False)

    delivery_address: Mapped[str]
    delivery_date: Mapped[datetime]
    is_delivered: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="orders")

    items: Mapped[list["Item"]] = relationship(
        back_populates="order",
        cascade="all, delete-orphan",
    )
