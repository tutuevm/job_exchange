import pytest

from src.database import async_session_maker
from src.models import Place


@pytest.mark.asyncio
async def test_create_model():
    async with async_session_maker() as session:
        new_record = Place(
            id="93169ada-d374-4152-addb-322412e335a3", title="Test Record"
        )
        session.add(new_record)
        await session.commit()

        result = await session.get(Place, new_record.id)
        assert result is not None
        assert result.title == "Test Record"
