from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.auth.security import get_password_hash
from src.user.models import User
from src.user.schemas import UserCreate


async def all_users(session: AsyncSession) -> list[User]:
    stmt = select(User)
    result = await session.execute(stmt)
    return list(result.scalars().all())


async def add_user(
    session: AsyncSession,
    user_in: UserCreate,
) -> User:
    user = User(
        username=user_in.username,
        email=user_in.email,
        hashed_password=get_password_hash(user_in.hashed_password),
    )
    session.add(user)
    await session.commit()
    await session.refresh(user)

    return user


async def get_user_by_email(
    session: AsyncSession,
    email: str,
) -> User | None:
    stmt = select(User).where(User.email == email)
    result = await session.execute(stmt)
    return result.scalar_one_or_none()
