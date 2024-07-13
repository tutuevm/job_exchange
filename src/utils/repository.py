from abc import ABC, abstractmethod
from typing import List

from sqlalchemy import select, insert, update
from sqlalchemy.ext.asyncio import AsyncSession


class AbstractRepository(ABC):

    @abstractmethod
    async def find_by_filter(self):
        raise NotImplementedError

    @abstractmethod
    async def add_one(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def get_all(self):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def find_by_filter(self, **filter_by) -> List:
        query = select(self.model).filter_by(**filter_by)
        result = await self.session.execute(query)
        result = [row[0] for row in result.all()]
        return result

    async def add_one(self, data: dict) -> int:
        stmt = insert(self.model).values(**data).returning(self.model.id)
        result = await self.session.execute(stmt)
        return result.scalar_one()

    async def get_all(self) -> List:
        query = select(self.model)
        result = await self.session.execute(query)
        result = [row[0] for row in result.all()]
        return result

    async def update_cell(self, filter_by: dict, values: dict):
        stmt = (update(self.model).where(**filter_by).values(**values))
        await self.session.execute(stmt)
        return {"status": "OK"}