import pytest
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from src.config import settings
from src.database import Base  # Импортируйте вашу базовую модель

TEST_DB_URL = f"postgresql+asyncpg://{settings.DB_SETTINGS.DB_USER}:{settings.DB_SETTINGS.DB_PASSWORD}@{settings.DB_SETTINGS.DB_HOST}:{settings.DB_SETTINGS.DB_PORT}/{settings.DB_SETTINGS.TEST_DB_NAME}"
engine_test = create_async_engine(TEST_DB_URL, echo=False)
async_session_maker = async_sessionmaker(engine_test, expire_on_commit=False)


@pytest.fixture(scope="session", autouse=True)
async def prepare_database():
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

