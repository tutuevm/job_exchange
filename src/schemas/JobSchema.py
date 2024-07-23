from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from datetime import datetime, timedelta
from enum import Enum


class JobSchema(BaseModel):
    id : UUID = Field(default_factory=uuid4)
    title : str = Field(max_length=100)
    price : int
    description: str = Field(max_length=400)
    started_at: datetime = Field(default=datetime.now())
    finished_at: datetime = Field(default=datetime.now() + timedelta(days=1))
    action_type: UUID
    location: UUID
    is_active: bool = Field(default=True)
    job_address: str = Field(max_length=200)
    owner_id: UUID
    organization_id : UUID


class JobStatus(Enum):
    DRAFT = 'Черновик'
    CREATED = 'Создана'
    UNDER_REVIEW = 'На проверке'
    COMPLETED = 'Выполнена'
    CLOSED = 'Закрыта'