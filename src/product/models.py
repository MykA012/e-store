from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from src.database.models.base import Base

if TYPE_CHECKING:
    from src.category.models import Category


class Product(Base):
    name: Mapped[str] = mapped_column(unique=True)

    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))    
    category: Mapped["Category"] = relationship(back_populates="products")
