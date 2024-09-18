from src.Notification.schemas import (
    NotificationMarkReadSchema,
    NotificationCreateSchema,
)
from src.utils.UnitOfWork import InterfaceUnitOfWork


class NotificationService:

    async def get_user_unread_notifications(
        self, uow: InterfaceUnitOfWork, current_user: dict
    ):
        async with uow:
            result = await uow.notification.return_unread_user_notif(
                user_id=current_user["id"]
            )
        return result

    async def mark_notifications_as_read(
        self, uow: InterfaceUnitOfWork, notif_list: NotificationMarkReadSchema
    ):
        notifications_list = notif_list.model_dump()["notifications"]
        async with uow:
            for notif in notifications_list:
                await uow.notification.update_notification(
                    notification_id=notif, update_data={"is_read": True}
                )
        return {"status": "OK"}

    async def create_notification(
        self, uow: InterfaceUnitOfWork, notification: NotificationCreateSchema
    ):
        notif_data = notification.model_dump()
        async with uow:
            await uow.notification.add_one(notif_data)
