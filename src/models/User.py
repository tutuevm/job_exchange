from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey, String, Table, Column, DateTime, Boolean, LargeBinary, func
from sqlalchemy.dialects.postgresql import UUID as alchemy_uuid
from uuid import UUID
from typing import List, TYPE_CHECKING
from datetime import datetime

from src.schemas.JobSchema import JobStatus

if TYPE_CHECKING:
    from src.models.Notifications import Notification

from src.database import Base
from src.schemas.JobResponseType import JobResponseType


user_attribute_association = Table(
    'user_attribute_association', Base.metadata,
    Column('user_id', alchemy_uuid, ForeignKey('users.id'), primary_key=True),
    Column('attribute_id', alchemy_uuid, ForeignKey('user_attributes.id'), primary_key=True),
)

user_job_association = Table(
    'user_job_association', Base.metadata,
    Column('user_id', alchemy_uuid, ForeignKey('users.id'), primary_key=True),
          Column('job_id', alchemy_uuid, ForeignKey('jobs.id'), primary_key=True),
          Column('status', String(50), default=JobResponseType.SUBMITTED.value ,nullable=False)
)

class User(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    attributes: Mapped[List["UserAttribute"]] = relationship("UserAttribute", secondary=user_attribute_association, back_populates='user' )
    full_name: Mapped[str] = mapped_column(String(50))
    login: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    email: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    hashed_password: Mapped[bytes] = mapped_column(LargeBinary)
    assigned_jobs: Mapped[List["Job"]] = relationship("Job", secondary=user_job_association, back_populates='responded_users')
    notifications: Mapped[List["Notification"]] = relationship(back_populates="user")
    created_jobs: Mapped[List["Job"]] = relationship(back_populates="owner")
    is_active : Mapped[bool] = mapped_column(default=True)


class UserAttribute(Base):
    __tablename__ = 'user_attributes'

    id: Mapped[UUID] = mapped_column(primary_key=True)
    key: Mapped[str] = mapped_column(String(50), nullable=False)
    value : Mapped[str] = mapped_column(String(50), nullable=False)

    user = relationship('User', secondary=user_attribute_association, back_populates='attributes')


class Job(Base):
    __tablename__ = 'jobs'
    id : Mapped[UUID] = mapped_column(primary_key=True)
    status: Mapped[str] = mapped_column(String(50), default=JobStatus.CREATED.value, index=True)
    # type : Mapped[str] = mapped_column(index=True)
    price : Mapped[int]
    title : Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(400))
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.now(),
    )
    started_at: Mapped[datetime] = mapped_column(DateTime)
    finished_at: Mapped[datetime] = mapped_column(DateTime)
    action_type: Mapped[UUID] = mapped_column(ForeignKey('action_types.id'))
    # location: Mapped[UUID] = mapped_column(ForeignKey('places.id')) #
    #city: Mapped[UUID] = mapped_column(ForeignKey('places.id'), index=True)
    #location : Mapped[str] = mapped_column(String(400))
    is_active: Mapped[bool] = mapped_column(Boolean, index=True,)
    organization_id: Mapped[UUID] = mapped_column(ForeignKey('organizations.id'))
    job_address: Mapped[str] = mapped_column(String(200))
    owner_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), index=True, nullable=False)

    responded_users: Mapped[List["User"]] = relationship('User', secondary=user_job_association, back_populates='assigned_jobs')
    owner: Mapped["User"] = relationship(back_populates="created_jobs")