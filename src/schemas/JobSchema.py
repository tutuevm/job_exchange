from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from datetime import datetime, timedelta


class JobSchema(BaseModel):
    id : UUID = Field(default_factory=uuid4)
    title : str = Field(max_length=100)
    price : int
    description: str = Field(max_length=400)
    finished_at: datetime = Field(default=datetime.now() + timedelta(days=1))
    action_type: UUID
    location: UUID
    is_active: bool = Field(default=True)