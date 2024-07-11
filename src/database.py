from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase


from src.config import DataBaseSettings

DB_URL = f"postgresql+asyncpg://{DataBaseSettings.DATABASE_USER}:{DataBaseSettings.DATABASE_PASSWORD}@{DataBaseSettings.DB_HOST}:{DataBaseSettings.DB_PORT}/{DataBaseSettings.DB_NAME}"

async_engine = create_async_engine(DB_URL)


async_session_maker = async_sessionmaker(
    async_engine,
    expire_on_commit=False
)

class Base(DeclarativeBase):
    __abstract__ = True
