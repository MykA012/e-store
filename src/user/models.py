from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import Base


class User(Base):
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]

    is_active: Mapped[bool] = mapped_column(default=True)
