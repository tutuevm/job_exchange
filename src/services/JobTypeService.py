from uuid import UUID

from src.utils.UnitOfWork import InterfaceUnitOfWork


class JobTypeService:
    async def create_job_type(self, uow: InterfaceUnitOfWork, title: str):
        data = {"title": title}
        async with uow:
            status = await uow.job_type.add_one(data)
        return status

    async def get_type_by_id(self, uow: InterfaceUnitOfWork, type_id: UUID):
        async with uow:
            result = await uow.job_type.find_by_filter(id=type_id)
        return result

    async def get_all_types(self, uow: InterfaceUnitOfWork):
        async with uow:
            result = await uow.job_type.get_all()
        return result
