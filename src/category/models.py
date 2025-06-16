from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import event
from unidecode import unidecode

from src.database.models.base import Base

if TYPE_CHECKING:
    from src.product.models import Product


class Category(Base):
    __tablename__ = "categories"

    name: Mapped[str] = mapped_column(unique=True)
    slug: Mapped[str] = mapped_column(unique=True, index=True)

    products: Mapped[list["Product"]] = relationship(back_populates="category")

    @staticmethod
    def generate_slug(name: str) -> str:
        slug = unidecode(name).strip().lower()
        slug = slug.replace(" ", "-")
        return slug


@event.listens_for(Category, "before_insert")
@event.listens_for(Category, "before_update")
def generate_category_slug(mapper, conn, target):
    target.slug = Category.generate_slug(target.name)
