from abc import ABC, abstractmethod
from typing import List, Any, Sequence

from sqlalchemy import select, insert, Row, RowMapping
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
        print(filter_by)
        query = select(self.model).filter_by(**filter_by)
        result = await self.session.execute(query)
        result = [row[0] for row in result.all()]
        return result

    async def add_one(self, data: dict) -> int:
        stmt = insert(self.model).values(**data).returning(self.model.id)
        result = await self.session.execute(stmt)
        return result.scalar_one()

    async def get_all(self) -> List:
        print(self.model)
        query = select(self.model)
        result = await self.session.execute(query)
        result = [row[0] for row in result.all()]
        return result
