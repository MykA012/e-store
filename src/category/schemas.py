from pydantic import BaseModel, ConfigDict

from src.product.schemas import ProductIDB


class CategoryBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str


class CategoryCreate(CategoryBase):
    pass


class CategoryPatch(BaseModel):
    name: str | None = None


class CategoryPut(CategoryBase):
    pass


class CategoryIDB(CategoryBase):
    id: int
    slug: str


class CategoryWithProducts(CategoryIDB):
    model_config = ConfigDict(from_attributes=True)
    products: list[ProductIDB]
