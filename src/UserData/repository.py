from src.utils.repository import SQLAlchemyRepository
from src.UserData.models import UserData


class UserDataRepository(SQLAlchemyRepository):
    model = UserData
