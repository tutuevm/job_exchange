from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase


from src.config import db_settings

DB_URL = f"postgresql+asyncpg://{db_settings.DB_USER}:{db_settings.DB_PASSWORD}@{db_settings.DB_HOST}:{db_settings.DB_PORT}/{db_settings.DB_NAME}"

async_engine = create_async_engine(echo=False, url=DB_URL)


async_session_maker = async_sessionmaker(
    async_engine,
    expire_on_commit=False
)

TEST_DB_URL = f"postgresql+asyncpg://{db_settings.DB_USER}:{db_settings.DB_PASSWORD}@{db_settings.DB_HOST}:{db_settings.DB_PORT}/{db_settings.TEST_DB_NAME}"

engine_test = create_async_engine(TEST_DB_URL)

test_session_maker = async_sessionmaker(engine_test, expire_on_commit=False)

class Base(DeclarativeBase):
    __abstract__ = True
