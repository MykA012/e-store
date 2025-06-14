from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import Sequence, select

from src.auth.utils import get_password_hash
from src.database.models.user import User
from src.schemas.user import UserCreate


async def create(session: AsyncSession, user_in: UserCreate) -> User:
    user = User(
        email=user_in.email,
        password=get_password_hash(user_in.password),
    )

    session.add(user)

    await session.commit()
    await session.refresh(user)

    return user


async def get_user_by_email(session: AsyncSession, email: str) -> User | None:
    stmt = select(User).where(User.email)
    result = await session.execute(stmt)
    return result.scalar_one_or_none()


async def all_users(session: AsyncSession) -> Sequence[User]:
    stmt = select(User)
    result = await session.execute(stmt)
    users = result.scalars().all()
    return users
