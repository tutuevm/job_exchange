from uuid import UUID

from src.utils.UnitOfWork import InterfaceUnitOfWork



class JobStatusService:

    async def create_job_status(self, uow: InterfaceUnitOfWork, title: str):
        data = {
            'title' : title
        }
        async with uow:
            status = await uow.job_status.add_one(data)
        return status

    async def get_status_by_id(self, uow: InterfaceUnitOfWork, status_id: UUID):
        async with uow:
            result = await uow.job_status.find_by_filter(id=status_id)
        return result

    async def get_all_statuses(self, uow: InterfaceUnitOfWork):
        async with uow:
            result = await uow.job_status.get_all()
        return result



