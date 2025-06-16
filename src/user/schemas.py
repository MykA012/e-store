from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    hashed_password: str


class UserCreate(UserBase):
    pass


class UserIDB(UserBase):
    id: int
