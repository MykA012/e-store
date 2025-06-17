from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, event
from unidecode import unidecode

from src.database.models.base import Base

if TYPE_CHECKING:
    from src.cart.models import Item
    from src.category.models import Category


class Product(Base):
    name: Mapped[str] = mapped_column(unique=True)
    slug: Mapped[str] = mapped_column(unique=True, index=True)
    price: Mapped[Decimal]

    item: Mapped["Item"] = relationship(back_populates="product")

    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    category: Mapped["Category"] = relationship(back_populates="products")

    @staticmethod
    def generate_slug(name: str) -> str:
        slug = unidecode(name).strip().lower()
        slug = slug.replace(" ", "-")
        return slug


@event.listens_for(Product, "before_insert")
@event.listens_for(Product, "before_update")
def generate_product_slug(mapper, conn, target):
    target.slug = Product.generate_slug(target.name)
