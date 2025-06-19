from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from src.config import load_settings


engine = create_async_engine(url=load_settings().db_url)

session_factory = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    autoflush=False,
)
