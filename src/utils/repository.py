from abc import ABC, abstractmethod
from typing import List

from fastapi import HTTPException, status
from sqlalchemy import select, insert, update, delete
from sqlalchemy.exc import IntegrityError
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

    @abstractmethod
    async def update_value(self, elem, **update_data):
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

    async def add_one(self, data: dict) -> dict:
        stmt = insert(self.model).values(**data)
        await self.session.execute(stmt)
        return {"status": "OK"}

    async def get_all(self) -> List:
        query = select(self.model)
        result = await self.session.execute(query)
        result = [row[0] for row in result.all()]
        return result


    async def delete_one(self, **filter_by):
        elem = await self.session.scalar(select(self.model).filter_by(**filter_by))
        if not elem:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'element with {filter_by} does not exist')
        stmt = delete(self.model).filter_by(**filter_by)
        await self.session.execute(stmt)
        return {'status': f'elem with {filter_by} deleted'}

    async def update_value(self, elem, **update_data):
        for key, value in update_data.items():
            if hasattr(elem, key):
                setattr(elem, key, value)
        return elem