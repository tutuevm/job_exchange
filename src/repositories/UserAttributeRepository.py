from src.models.User import UserAttribute
from src.utils.repository import SQLAlchemyRepository


class UserAttributeRepository(SQLAlchemyRepository):
    model = UserAttribute