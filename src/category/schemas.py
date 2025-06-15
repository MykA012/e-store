from pydantic import BaseModel


class CategoryBase(BaseModel):
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
