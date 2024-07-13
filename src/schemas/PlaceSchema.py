from pydantic import BaseModel, Field
from uuid import UUID, uuid4
class PlaceSchema(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title : str = Field(None, max_length=100)