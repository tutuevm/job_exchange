from typing import List
from uuid import UUID

from pydantic import BaseModel, Field


class NotificationCreateSchema(BaseModel):
    notification_data: str = Field(max_length=400)
    user_id: UUID = Field()


class NotificationMarkReadSchema(BaseModel):
    notifications: List[UUID]
