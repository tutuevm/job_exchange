from uuid import UUID

import pytest

from src.schemas.PlaceSchema import PlaceSchema
from src.services.PlaceService import PlaceService
from src.utils.UnitOfWork import UnitOfWork


class TestPlaceService:
    @pytest.mark.asyncio
    async def test_add_place(self):
        place = PlaceSchema(
            id="93169ada-d374-4152-addb-322412e335a3", title="Test Record"
        )
        result = await PlaceService().add_place(UnitOfWork(), place=place)
        assert result == {"status": "OK"}

    @pytest.mark.asyncio
    async def test_get_place_by_id(self):
        uow = UnitOfWork()
        result = await PlaceService().get_place_by_id(
            uow=uow, id=UUID("93169ada-d374-4152-addb-322412e335a3")
        )
        assert len(result) == 1
