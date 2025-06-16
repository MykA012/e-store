from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    hashed_password: str


class UserEdit(BaseModel):
    username: str | None = None
    email: EmailStr | None = None


class UserChangePassword(BaseModel):
    hashed_password: str | None = None


class UserIDB(UserBase):
    id: int
