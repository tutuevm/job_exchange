from src.schemas.ActionTypeScheme import ActionTypeSchema
from src.utils.UnitOfWork import InterfaceUnitOfWork
class ActionTypeService:
    async def add_type(self,  uow:InterfaceUnitOfWork, type_schema : ActionTypeSchema):
        data = type_schema.model_dump()
        async with uow:
            type_id = await uow.action_type.add_one(data)
            return type_id

    async def get_type_by_id(self, uow:InterfaceUnitOfWork, id : int):
        pass