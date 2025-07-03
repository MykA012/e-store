from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.base import Base

if TYPE_CHECKING:
    from src.cart.models import Cart
    from src.order.models import Order


class User(Base):
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]
    is_active: Mapped[bool] = mapped_column(default=True)
    is_admin: Mapped[bool] = mapped_column(default=False)

    cart: Mapped["Cart"] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
        uselist=False,
    )
    orders: Mapped[list["Order"]] = relationship(
        back_populates="user",
        cascade="all, delete orphan",
    )
