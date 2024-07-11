from sqlalchemy.ext.asyncio import  async_sessionmaker, create_async_engine
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase, declared_attr
from contextlib import contextmanager

from src.config import DataBaseSettings


DATABASE_URL = f"postgresql+asyncpg://{DataBaseSettings.DB_USER}:{DataBaseSettings.DB_PASS}@{DataBaseSettings.DB_HOST}:{DataBaseSettings.DB_PORT}/{DataBaseSettings.DB_NAME}"


engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

class Base(DeclarativeBase):
    __abstract__ = True
    @declared_attr.directive
    def __tablename__ (cls) -> str:
        return f'{cls.__name__.lower()}'



async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session



