from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import Base


class User(Base):
    username: Mapped[str]

    email: Mapped[str] = mapped_column(unique=True)

    password: Mapped[str]
