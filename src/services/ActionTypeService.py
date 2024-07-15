from uuid import UUID

from typing import List
from src.schemas.ActionTypeScheme import ActionTypeSchema
from src.utils.UnitOfWork import InterfaceUnitOfWork


class ActionTypeService:
    async def add_type(self, uow: InterfaceUnitOfWork, type_schema: ActionTypeSchema) -> dict:
        data = type_schema.model_dump()
        async with uow:
            status = await uow.action_type.add_one(data)
            return status

    async def get_type_by_id(self, uow: InterfaceUnitOfWork, type_id: UUID) -> List:
        async with uow:
            type_title = await uow.action_type.find_by_filter(id=type_id)
        return type_title
