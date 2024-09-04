from uuid import UUID, uuid4

import pytest
from httpx import AsyncClient

from src.Place.models import Place
from src.Place.schemas import PlaceSchema
from src.Place.services import PlaceService
from src.database import async_session_maker
from src.utils.UnitOfWork import UnitOfWork


class TestPlaceRouter:
    @pytest.mark.asyncio
    async def test_get_all(self, ac: AsyncClient):
        result = await ac.get("/place/get_all")
        assert result.status_code == 200
        assert type(result.json()) == list

    @pytest.mark.asyncio
    async def test_add_place(self, ac: AsyncClient):
        result = await ac.post("/place/add_place", json={"title": "Казань"})
        assert result.status_code == 200
        assert result.json() == {"status": "OK"}

    async def test_get_place_by_id(self, ac: AsyncClient):
        uuid = uuid4()
        async with async_session_maker() as session:
            new_record = Place(id=uuid, title="Киров")
            session.add(new_record)
            await session.commit()
        result = await ac.post("/place/get_place_by_id", json={"id": str(uuid)})
        assert result.json()[0]["title"] == "Киров"


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
