from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from src.database.models.base import Base

if TYPE_CHECKING:
    from src.user.models import User
    from src.product.models import Product


class Cart(Base):
    items_count: Mapped[int] = mapped_column(default=0)
    total_price: Mapped[Decimal] = mapped_column(default=0)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="cart")

    items: Mapped[list["Item"]] = relationship(
        back_populates="cart",
        cascade="all, delete-orphan",
    )


class Item(Base):
    quantity: Mapped[int]

    cart_id: Mapped[int] = mapped_column(ForeignKey("carts.id"))
    cart: Mapped["Cart"] = relationship(back_populates="items")

    product: Mapped["Product"] = relationship(back_populates="item")
