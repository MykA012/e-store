from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import Sequence, select

from src.database.models.user import User
from src.schemas.user import UserCreate


async def create(session: AsyncSession, user_in: UserCreate) -> User:
    user = User(**user_in.model_dump())

    session.add(user)

    await session.commit()
    await session.refresh(user)

    return user


async def all_users(session: AsyncSession) -> Sequence[User]:
    stmt = select(User)
    result = await session.execute(stmt)
    users = result.scalars().all()
    return users
