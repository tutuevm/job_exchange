from typing import List
from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy import select, or_, Row, and_, update, insert, func
from sqlalchemy.orm import selectinload, aliased, joinedload

from src.Job.models import Job
from src.User.models import User, user_job_association, user_attribute_association
from src.UserRating.models import UserRating
from src.utils.repository import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository):
    model = User

    async def get_all_user(self) -> List:
        query = (
            select(self.model, func.avg(UserRating.rating_value).label("user_rating"))
            .outerjoin(UserRating, User.id == UserRating.user_id)
            .group_by(User.id)
            .options(selectinload(User.user_data))
            .where(User.manager_data == None)
        )
        result = await self.session.execute(query)
        res = []
        for row in result.all():
            row[0].user_rating = row[1]
            res.append(row[0])
        return res

    async def get_user_by_id(self, user_id):
        query = (
            select(User, func.avg(UserRating.rating_value).label("user_rating"))
            .outerjoin(UserRating, User.id == UserRating.user_id)
            .where(User.id == user_id)
            .group_by(User.id)
            .options(selectinload(User.user_data))
            .options(selectinload(User.manager_data))
        )
        result = (await self.session.execute(query)).all()
        if result:
            result = result[0]
            result[0].user_rating = result[1]
            return result[0]
        return result

        # return result

    async def append_many_to_many_elem(
        self, user_id, elem_model, elem_id, row_name
    ) -> dict:
        user = await self.session.scalar(
            select(self.model)
            .filter_by(id=user_id)
            .options(selectinload(getattr(User, row_name)))
            .options(selectinload(User.user_data))
        )
        elem = await self.session.scalar(select(elem_model).filter_by(id=elem_id))
        user_relationship = getattr(user, row_name)
        if elem in user_relationship:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="relationship is already exist",
            )
        user_relationship.append(elem)
        return {"user": user, "elem": elem}

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

    async def create_user(self, user_data) -> str:
        stmt = insert(self.model).values(**user_data).returning(User.id)
        result = await self.session.execute(stmt)
        id = result.scalar_one()
        return id

    async def get_users_by_different_fields(self, *filter_by) -> List[User]:
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
        query = (
            select(Job, user_job_association.c.user_id, User.full_name)
            .outerjoin(
                user_job_association,
                and_(
                    user_job_association.c.job_id == Job.id,
                    user_job_association.c.response_status == "ACCEPTED",
                ),
            )
            .outerjoin(User, User.id == user_job_association.c.user_id)
            .where(Job.owner_id == owner_id)
            .options(joinedload(Job.action_type))
            .options(joinedload(Job.city))
            .options(joinedload(Job.organization))
        )
        result = await self.session.execute(query)
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


class UserAttrAssociationRepository(SQLAlchemyRepository):
    model = user_attribute_association
