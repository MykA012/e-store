from pydantic import BaseModel, ConfigDict


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
