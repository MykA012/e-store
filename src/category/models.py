from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from src.database.models.base import Base

if TYPE_CHECKING:
    from src.product.models import Product


class Category(Base):
    __tablename__ = "categories"

    name: Mapped[str] = mapped_column(unique=True)

    products: Mapped[list["Product"]] = relationship(back_populates="category")
