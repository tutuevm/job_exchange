from typing import List

from sqlalchemy import select, and_

from src.Notification.models import Notification
from src.utils.repository import SQLAlchemyRepository


class NotificationsRepository(SQLAlchemyRepository):
    model = Notification

    async def return_unread_user_notif(self, user_id) -> List[Notification]:
        query = select(self.model).where(
            and_(Notification.user_id == user_id, Notification.is_read == False)
        )
        res = await self.session.execute(query)
        result = [row[0] for row in res.all()]
        return result
