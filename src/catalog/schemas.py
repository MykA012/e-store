from pydantic import BaseModel, ConfigDict

from src.product.schemas import ProductIDB
from src.category.schemas import CategoryIDB


class CategoryWithProducts(CategoryIDB):
    model_config = ConfigDict(from_attributes=True)
    products: list[ProductIDB]
