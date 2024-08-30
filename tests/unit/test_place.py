from uuid import UUID

import pytest

from src.database import async_session_maker
from src.models import Place
from src.schemas.PlaceSchema import PlaceSchema
from src.services.PlaceService import PlaceService
from src.utils.UnitOfWork import UnitOfWork


class TestPlaceService:

    @pytest.mark.asyncio
    async def test_add_place(self):
        place = PlaceSchema(id="93169ada-d374-4152-addb-322412e335a3", title="Ижевск")
        result = await PlaceService().add_place(UnitOfWork(), place=place)
        assert result == {"status": "OK"}

    @pytest.mark.asyncio
    async def test_get_place_by_id(self):
        async with async_session_maker() as session:
            new_record = Place(
                id="16739ada-d374-4152-addb-322412e335a3", title="Test Record"
            )
            session.add(new_record)
            await session.commit()
        result = await PlaceService().get_place_by_id(
            uow=UnitOfWork(), id=UUID("16739ada-d374-4152-addb-322412e335a3")
        )
        assert len(result) == 1

    @pytest.mark.asyncio
    async def test_get_all(self):
        result = await PlaceService().get_all(UnitOfWork())
        assert type(result) == list
