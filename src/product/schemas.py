from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    price: Decimal

    category_id: int


class ProductCreate(ProductBase):
    pass


class ProductPatch(BaseModel):
    name: str | None = None
    price: Decimal | None = None

    category_id: int | None = None


class ProductPut(ProductBase):
    pass


class ProductIDB(ProductBase):
    id: int
    slug: str
