from src.utils.UnitOfWork import InterfaceUnitOfWork


class NotificationService:

    async def get_user_unread_notifications(
        self, uow: InterfaceUnitOfWork, current_user
    ):
        async with uow:
            result = await uow.notification.return_unread_user_notif(
                user_id=current_user["id"]
            )
        return result
