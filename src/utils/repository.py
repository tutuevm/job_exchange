from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession

class AbstractRepository(ABC):

    @abstractmethod
    async def get_by_id(self):
        raise NotImplementedError

    @abstractmethod
    async def add_one(self):
        raise NotImplementedError

    @abstractmethod
    async def get_all(self):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session : AsyncSession):
        self.session = session

    async def get_by_id(self, **filter_by):
        pass


    async def add_one(self):
        pass


    async def get_all(self):
        pass
