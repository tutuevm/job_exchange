from pydantic import BaseModel, Field

from uuid import UUID, uuid4

from sqlalchemy import String


class ActionTypeSchema(BaseModel):
    id : UUID = Field(default_factory=uuid4)
    title: str = Field(None, max_length=50)