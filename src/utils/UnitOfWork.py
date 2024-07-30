from typing import Type


from src.database import async_session_maker, test_session_maker
from src.repositories.RActionType import ActionTypeRepository
from src.repositories.RJob import JobRepository
from src.repositories.RPlace import PlaceRepository
from src.repositories.RTransaction import TransactionRepository
from src.repositories.RUser import UserRepository
from src.repositories.UserAttributeRepository import UserAttributeRepository
from src.repositories.ROrganization import OrganizationRepository
from src.repositories.RJobUserAssociation import UserJobAssociationRepository


class InterfaceUnitOfWork:
        place: Type[PlaceRepository]
        action_type: Type[ActionTypeRepository]
        user_attr: Type[UserAttributeRepository]
        user : Type[UserRepository]
        job : Type[JobRepository]
        org : Type[OrganizationRepository]
        user_job_association: Type[UserJobAssociationRepository]
        transaction : Type[TransactionRepository]

        async def __aenter__(self):
            ...

        async def __aexit__(self, *args):
            ...

        async def commit(self):
            ...
        async def rollback(self):
            ...



class UnitOfWork:

    def __init__(self):
        self.session_maker = async_session_maker

    async def __aenter__(self):
        self.session = self.session_maker()

        self.place = PlaceRepository(self.session)
        self.action_type = ActionTypeRepository(self.session)
        self.user_attr = UserAttributeRepository(self.session)
        self.user = UserRepository(self.session)
        self.job = JobRepository(self.session)
        self.org = OrganizationRepository(self.session)
        self.user_job_association = UserJobAssociationRepository(self.session)
        self.transaction = TransactionRepository(self.session)

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            await self.rollback()
        else:
            await self.commit()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()


class TestsUnitOfWork:
    def __init__(self):
        self.session_maker = test_session_maker

    async def __aenter__(self):
        self.session = self.session_maker()

        self.place = PlaceRepository(self.session)
        self.action_type = ActionTypeRepository(self.session)
        self.user_attr = UserAttributeRepository(self.session)
        self.user = UserRepository(self.session)


    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            await self.rollback()
        else:
            await self.commit()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
