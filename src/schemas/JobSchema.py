from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from datetime import datetime, timedelta
from enum import Enum



class JobSchema(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    status:UUID
    type:UUID
    title: str = Field(max_length=100)
    ''' type: JobType = Field(JobType.HOURLY_PAYMENT.value)'''
    price: int
    description: str = Field(max_length=400)
    started_at: datetime = Field(default=datetime.now())
    finished_at: datetime = Field(default=datetime.now() + timedelta(days=1))
    action_type: UUID
    city: UUID
    job_location: str = Field(max_length=400)
    is_active: bool = Field(default=True)
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
