from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from src.config import settings

DB_URL = f"postgresql+asyncpg://{settings.DB_SETTINGS.DB_USER}:{settings.DB_SETTINGS.DB_PASSWORD}@{settings.DB_SETTINGS.DB_HOST}:{settings.DB_SETTINGS.DB_PORT}/{settings.DB_SETTINGS.DB_NAME}"

async_engine = create_async_engine(echo=False, url=DB_URL)

async_session_maker = async_sessionmaker(async_engine, expire_on_commit=False)


class Base(DeclarativeBase):
    __abstract__ = True
