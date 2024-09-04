from src.UserAttribute.models import UserAttribute
from src.utils.repository import SQLAlchemyRepository


class UserAttributeRepository(SQLAlchemyRepository):
    model = UserAttribute
