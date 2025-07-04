from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from src.database.models.base import Base

if TYPE_CHECKING:
    from src.user.models import User
    from src.product.models import Product
    from src.order.models import Order


class Cart(Base):
    items_count: Mapped[int] = mapped_column(default=0)
    total_price: Mapped[Decimal] = mapped_column(default=Decimal("0"))

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="cart")

    items: Mapped[list["Item"]] = relationship(
        back_populates="cart",
        cascade="all, delete-orphan",
    )


class Item(Base):
    quantity: Mapped[int]

    cart_id: Mapped[int | None] = mapped_column(ForeignKey("carts.id"))
    cart: Mapped["Cart | None"] = relationship(back_populates="items")

    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    product: Mapped["Product"] = relationship(back_populates="item")

    order_id: Mapped[int | None] = mapped_column(ForeignKey("orders.id"))
    order: Mapped["Order | None"] = relationship(back_populates="items")
