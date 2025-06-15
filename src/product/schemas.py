from decimal import Decimal

from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    slug: str
    price: Decimal

    category_id: int


class ProductCreate(ProductBase):
    pass


class ProductPatch(BaseModel):
    name: str | None = None
    slug: str | None = None
    price: Decimal | None = None

    category_id: int | None = None


class ProductPut(ProductBase):
    pass


class ProductIDB(ProductBase):
    id: int
