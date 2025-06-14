from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from src.config import load_settings


engine = create_async_engine(url=load_settings().db_url)

session_factory = async_sessionmaker(bind=engine)


@asynccontextmanager
async def init_db(app: FastAPI):
    from src.database.models.base import Base
    from src.database.models import user
    
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    yield
