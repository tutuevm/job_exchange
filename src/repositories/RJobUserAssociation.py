from sqlalchemy import select, or_
from sqlalchemy.orm import selectinload
from uuid import UUID

from src.utils.repository import SQLAlchemyRepository
from src.models.User import user_job_association




class UserJobAssociationRepository(SQLAlchemyRepository):
    model = user_job_association



