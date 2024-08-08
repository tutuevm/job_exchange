from fastapi import HTTPException
from sqlalchemy import select, and_
from sqlalchemy.orm import selectinload, joinedload
from uuid import UUID

from starlette import status

from src.schemas.JobSchema import JobFilter
from src.utils.repository import SQLAlchemyRepository
from src.models.User import Job



class JobRepository(SQLAlchemyRepository):
    model = Job

    async def get_relationship(self, job_id: UUID, row_name: str):
        job = await self.session.scalar(
            select(self.model).filter_by(id=job_id).options(selectinload(getattr(Job, row_name))))
        if not job:
            HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'warning' : 'nothing found'})
        return getattr(job, row_name)




    async def get_jobs_by_filter(self, filter : JobFilter):
        '''Исправить это, пока никто не увидел'''
        query = select(Job)
        conditions = []

        if filter['owner_id']:
            conditions.append(self.model.owner_id == filter['owner_id'])
        if filter['location_id']:
            conditions.append(self.model.job_location.in_(filter['location_id']))
        if filter['action_type_id']:
            conditions.append(self.model.action_type.in_(filter['action_type_id']))
        if filter['price_min'] is not None:
            conditions.append(Job.price >= filter['price_min'])
        if filter['price_max'] is not None:
            conditions.append(Job.price <= filter['price_max'])

        if conditions:
            query = query.where(and_(*conditions))

        query = query.offset(filter['skip']).limit(filter['limit']).options(
            joinedload(Job.action_type)
        ).options(joinedload(Job.city)).options(joinedload(Job.organization))

        result = await self.session.execute(query)
        jobs = result.scalars().all()
        return jobs