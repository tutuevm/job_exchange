from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy import select, or_, Row, and_, update
from sqlalchemy.orm import selectinload, aliased, joinedload

from src.Job.models import Job
from src.Job.schemas import JobResponseType
from src.User.models import User, user_job_association
from src.utils.repository import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository):
    model = User

    async def append_many_to_many_elem(
        self, user_id, elem_model, elem_id, row_name
    ) -> dict:
        user = await self.session.scalar(
            select(self.model)
            .filter_by(id=user_id)
            .options(selectinload(getattr(User, row_name)))
        )
        elem = await self.session.scalar(select(elem_model).filter_by(id=elem_id))
        user_relationship = getattr(user, row_name)
        if elem in user_relationship:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="relationship is already exist",
            )
        user_relationship.append(elem)
        return user_relationship

    async def remove_many_to_many_elem(
        self, user_id, elem_model, elem_id, row_name
    ) -> dict:
        user = await self.session.scalar(
            select(self.model)
            .filter_by(id=user_id)
            .options(selectinload(getattr(User, row_name)))
        )
        elem = await self.session.scalar(select(elem_model).filter_by(id=elem_id))
        user_relationship = getattr(user, row_name)
        if elem not in user_relationship:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="relation does not exist",
            )
        user_relationship.remove(elem)
        return {"status": "OK"}

    async def get_users_by_different_fields(self, *filter_by):
        query = select(self.model).where(or_(*filter_by))
        result = await self.session.execute(query)
        result = [row[0] for row in result.all()]
        return result

    async def get_all_relationship_elements(self, user_id, row_name) -> dict:
        user = await self.session.scalar(
            select(self.model)
            .filter_by(id=user_id)
            .options(selectinload(getattr(User, row_name)))
        )
        user_relationship = getattr(user, row_name)
        return user_relationship

    async def get_user_assigned_jobs_with_status(self, user_id: UUID):
        results = await self.session.execute(
            select(Job, user_job_association.c.response_status)
            .join(user_job_association, Job.id == user_job_association.c.job_id)
            .filter(user_job_association.c.user_id == user_id)
            .options(joinedload(Job.action_type))
            .options(joinedload(Job.city))
            .options(joinedload(Job.organization))
        )

        jobs = results.all()
        return [{"job": row[0], "status": row[1]} for row in jobs]

    async def get_user_created_jobs_with_responded_user(self, owner_id):
        user_job_alias = aliased(user_job_association)
        stmt = (
            select(
                Job,
                User.id.label("responded_user_id"),
                User.full_name.label("responded_user_full_name"),
            )
            .outerjoin(user_job_alias, Job.id == user_job_alias.c.job_id)
            .outerjoin(User, User.id == user_job_alias.c.user_id)
            .filter(Job.owner_id == owner_id)
            .filter(
                (user_job_alias.c.response_status == JobResponseType.ACCEPTED)
                | (user_job_alias.c.response_status.is_(None))
            )
            .options(joinedload(Job.action_type))
            .options(joinedload(Job.city))
            .options(joinedload(Job.organization))
        )

        result = await self.session.execute(stmt)
        return [
            {"job": row[0], "responded_user": {"id": row[1], "full_name": row[2]}}
            for row in result.all()
        ]


class UserJobAssociationRepository(SQLAlchemyRepository):
    model = user_job_association

    async def get_association(self, user_id: UUID, job_id: UUID) -> Row:
        query = select(self.model).where(
            and_(self.model.c.user_id == user_id, self.model.c.job_id == job_id)
        )
        result = await self.session.execute(query)
        return result.all()[0]

    async def change_status_association(self, user_id: UUID, job_id: UUID, status):
        stmt = (
            update(self.model)
            .where(and_(self.model.c.user_id == user_id, self.model.c.job_id == job_id))
            .values(response_status=status)
        )
        result = await self.session.execute(stmt)
        return result
