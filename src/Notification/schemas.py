from pydantic import BaseModel, Field
from uuid import UUID


class NotificationCreateSchema(BaseModel):
    notification_data: str = Field(max_length=400)
    user_id: UUID = Field()
