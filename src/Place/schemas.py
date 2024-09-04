from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class PlaceSchema(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title : str = Field(None, max_length=100)

class PlaceByIdSchema(BaseModel):
    id: UUID