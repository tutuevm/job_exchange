from uuid import UUID

from pydantic import BaseModel, Field


class UserRatingCreateSchema(BaseModel):
    user_id: UUID = Field(description="Поле пользовтеля, которому выставляется рейтинг")
    rated_by: UUID = Field(description="Поле пользовтеля, который выставляет рейтинг")
    rating_value: float = Field(lt=5, ge=1)
    comment: str = Field(max_length=100)
