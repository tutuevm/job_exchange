from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from datetime import datetime, timedelta
from enum import Enum



class JobType(Enum):
    HOURLY_PAYMENT = "Почасовая оплата"
    SALARY = "Оплата по факту выполненной работы"

class JobStatus(Enum):
    DRAFT = 'Черновик'
    CREATED = 'Создана'
    UNDER_REVIEW = 'На проверке'
    COMPLETED = 'Выполнена'
    CLOSED = 'Закрыта'

class JobSchema(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str = Field(max_length=100)
    ''' type: JobType = Field(JobType.HOURLY_PAYMENT.value)'''
    price: int
    description: str = Field(max_length=400)
    started_at: datetime = Field(default=datetime.now())
    finished_at: datetime = Field(default=datetime.now() + timedelta(days=1))
    action_type: UUID
    location: UUID
    is_active: bool = Field(default=True)
    job_address: str = Field(max_length=200)
    owner_id: UUID
    organization_id: UUID



class JobFilter(BaseModel):
    owner_id: UUID | None = Field(None)
    location_id: UUID | None = Field(None)
    action_type_id: UUID | None = Field(None)
    price_min: int | None = Field(None)
    price_max: int | None = Field(None)
    skip : int = 0
    limit: int = 10
