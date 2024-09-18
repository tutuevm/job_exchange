from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class UserRatingCreateSchema(BaseModel):
    user_id: UUID = Field(description="Поле пользовтеля, которому выставляется рейтинг")
    rating_value: float = Field(le=5, ge=1)
    comment: Optional[None | str] = Field(max_length=100, default=None)
