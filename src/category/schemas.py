from pydantic import BaseModel, ConfigDict


class CategoryBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    slug: str


class CategoryCreate(CategoryBase):
    pass


class CategoryPatch(BaseModel):
    name: str | None = None
    slug: str | None = None


class CategoryPut(CategoryBase):
    pass


class CategoryIDB(CategoryBase):
    id: int
