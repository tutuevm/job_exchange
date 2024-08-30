from datetime import datetime, timedelta
from enum import Enum
from typing import List
from uuid import UUID, uuid4

from fastapi import Query
from pydantic import BaseModel, Field


class JobTypeSchema(Enum):
    HOURLY_PAY = "Почасовая оплата"
    SALARY = "Оплата по факту выаолнения работы"


class JobStatusSchema(Enum):
    DRAFT = "Черновик"
    CRATED = "Создана"
    ANDER_REVIEW = "На проверке"
    COMPLETED = "Выполнена"
    CLOSED = "Закрыта"


class JobSchema(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    status_value: JobStatusSchema
    type_value: JobTypeSchema
    title: str = Field(max_length=100)
    price: int
    description: str = Field(max_length=400)
    started_at: datetime = Field(default=datetime.now())
    finished_at: datetime = Field(default=datetime.now() + timedelta(days=1))
    action_type_id: UUID
    city_id: UUID
    job_location: str = Field(max_length=400)
    is_active: bool = Field(default=True)
    owner_id: UUID
    organization_id: UUID


class OrganizationSchema(BaseModel):
    id: UUID
    title: str


class ActionTypeSchema(BaseModel):
    id: UUID
    title: str


class CitySchema(BaseModel):
    id: UUID
    title: str


class JobResponseSchema(BaseModel):
    id: UUID
    price: int
    title: str
    description: str
    created_at: datetime
    started_at: datetime
    finished_at: datetime
    job_location: str
    is_active: bool
    owner_id: UUID
    organization: OrganizationSchema
    city: CitySchema
    action_type: ActionTypeSchema
    type_value: str
    status_value: str


class JobFilter(BaseModel):
    owner_id: UUID | None = Field(Query(None))
    location_id: List[UUID] | None = Field(Query(None))
    action_type_id: List[UUID] | None = Field(Query(None))
    price_min: int | None = Field(Query(None))
    price_max: int | None = Field(Query(None))
    skip: int = 0
    limit: int = 10


async def return_filter(
    owner_id: UUID | None = None,
    location_id: List[UUID] = Query(None),
    action_type_id: List[UUID] = Query(None),
    price_min: int | None = Query(None),
    price_max: int | None = Query(None),
    skip: int = 0,
    limit: int = 100,
):
    return {
        "owner_id": owner_id,
        "location_id": location_id,
        "action_type_id": action_type_id,
        "price_min": price_min,
        "price_max": price_max,
        "skip": skip,
        "limit": limit,
    }
