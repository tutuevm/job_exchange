from pydantic import BaseModel, Field
from uuid import UUID, uuid4
class AttributeSchema(BaseModel):
    id : UUID = Field(default_factory=uuid4)
    key : str = Field(None, max_length=50)
    value : str = Field(None, max_length=50)