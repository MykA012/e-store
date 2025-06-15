from typing import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncSession

from src.database.core import session_factory


async def session_dep() -> AsyncIterator[AsyncSession]:
    async with session_factory() as session:
        yield session
        await session.close()
