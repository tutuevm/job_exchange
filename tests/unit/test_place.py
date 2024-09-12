from uuid import UUID

import pytest
from pytest_mock import MockerFixture

from src.Place.schemas import PlaceSchema
from src.Place.services import PlaceService
from src.utils.UnitOfWork import InterfaceUnitOfWork


class TestPlaceService:
    place_instance = PlaceService()

    @pytest.mark.asyncio
    async def test_add_place(self, mocker: MockerFixture):
        mock_uow = mocker.AsyncMock(spec=InterfaceUnitOfWork)
        mock_place = mocker.Mock()
        mock_uow.place = mock_place
        mock_add_one = mocker.AsyncMock(return_value={"status": "success"})
        mock_place.add_one = mock_add_one
        place_data = {"title": "Test Place"}
        place = PlaceSchema(**place_data)
        result = await self.place_instance.add_place(uow=mock_uow, place=place)
        mock_add_one.assert_called_once_with(place.model_dump())
        assert result == {"status": "success"}
        mock_uow.__aenter__.assert_awaited_once()
        mock_uow.__aexit__.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_get_place_by_id(self, mocker: MockerFixture):
        mock_filter = mocker.AsyncMock(
            return_value=[
                {"title": "Test Place", "id": "47a9af15-9cd3-426e-99e3-79d761ffcaa7"}
            ]
        )
        mock_place = mocker.Mock()
        mock_uow = mocker.AsyncMock(spec=InterfaceUnitOfWork)
        mock_place.find_by_filter = mock_filter
        mock_uow.place = mock_place
        result = await self.place_instance.get_place_by_id(
            uow=mock_uow, id=UUID("47a9af15-9cd3-426e-99e3-79d761ffcaa7")
        )
        assert result == [
            {"title": "Test Place", "id": "47a9af15-9cd3-426e-99e3-79d761ffcaa7"}
        ]
        mock_uow.__aenter__.assert_awaited_once()
        mock_uow.__aexit__.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_get_all(self, mocker: MockerFixture):
        mock_get_all = mocker.AsyncMock(
            return_value=[
                {"title": "Test Place", "id": "47a9af15-9cd3-426e-99e3-79d761ffcaa7"}
            ]
        )
        mock_place = mocker.Mock()
        mock_uow = mocker.AsyncMock(spec=InterfaceUnitOfWork)
        mock_place.get_all = mock_get_all
        mock_uow.place = mock_place
        result = await self.place_instance.get_all(uow=mock_uow)
        assert result == [
            {"title": "Test Place", "id": "47a9af15-9cd3-426e-99e3-79d761ffcaa7"}
        ]
        mock_uow.__aenter__.assert_awaited_once()
        mock_uow.__aexit__.assert_awaited_once()
