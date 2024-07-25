from fastapi import Query
from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from datetime import datetime, timedelta
from typing import Optional, List


class JobSchema(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    status:UUID
    type:UUID
    title: str = Field(max_length=100)
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
    owner_id: UUID | None = Field(Query(None))
    location_id : List[UUID] | None = Field(Query(None))
    action_type_id: List[UUID] | None = Field(Query(None))
    price_min: int | None = Field(Query(None))
    price_max: int | None = Field(Query(None))
    skip : int = 0
    limit: int = 10


async def return_filter(
        owner_id: UUID | None = None,
        location_id : List[UUID] = Query(None),
        action_type_id: List[UUID]  = Query(None),
        price_min: int | None = Query(None),
        price_max: int | None = Query(None),
        skip: int = 0,
        limit: int = 100):
    return {"owner_id": owner_id, "location_id": location_id,'action_type_id':action_type_id,'price_min':price_min,'price_max':price_max, "skip": skip, "limit": limit}