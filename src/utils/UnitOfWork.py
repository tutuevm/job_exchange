from typing import Type

from src.ActionType.repository import ActionTypeRepository
from src.Job.repository import JobRepository
from src.Notification.repository import NotificationsRepository
from src.Organization.repository import OrganizationRepository
from src.Place.repository import PlaceRepository
from src.Transaction.repository import TransactionRepository
from src.User.repository import UserRepository, UserJobAssociationRepository
from src.UserAttribute.repository import UserAttributeRepository
from src.UserData.repository import UserDataRepository
from src.database import async_session_maker


class InterfaceUnitOfWork:
    place: Type[PlaceRepository]
    action_type: Type[ActionTypeRepository]
    user_attr: Type[UserAttributeRepository]
    user: Type[UserRepository]
    job: Type[JobRepository]
    org: Type[OrganizationRepository]
    user_job_association: Type[UserJobAssociationRepository]
    transaction: Type[TransactionRepository]
    user_data: Type[UserDataRepository]
    notification: Type[NotificationsRepository]

    async def __aenter__(self): ...

    async def __aexit__(self, *args): ...

    async def commit(self): ...
    async def rollback(self): ...


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
        self.user_data = UserDataRepository(self.session)
        self.notification = NotificationsRepository(self.session)

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
