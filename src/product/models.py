from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from src.database.models.base import Base

if TYPE_CHECKING:
    from src.category.models import Category


class Product(Base):
    name: Mapped[str] = mapped_column(unique=True)
    slug: Mapped[str] = mapped_column(unique=True, index=True)
    price: Mapped[Decimal] = mapped_column(default=0, server_default=0)

    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))    
    category: Mapped["Category"] = relationship(back_populates="products")
