from src.models.ActionType import ActionType
from src.utils.repository import SQLAlchemyRepository


class ActionTypeRepository(SQLAlchemyRepository):
    model = ActionType
