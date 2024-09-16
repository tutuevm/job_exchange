from src.utils.repository import SQLAlchemyRepository
from src.Notification.models import Notification


class NotificationsRepository(SQLAlchemyRepository):
    model = Notification
