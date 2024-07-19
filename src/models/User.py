from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey, String, Table, Column, DateTime, Boolean, LargeBinary, func
from sqlalchemy.dialects.postgresql import UUID as alchemy_uuid
from uuid import UUID
from typing import List
from datetime import datetime
from uuid import uuid4

from src.database import Base

user_attribute_association = Table(
    'user_attribute_association', Base.metadata,
    Column('user_id', alchemy_uuid, ForeignKey('users.id'), primary_key=True),
    Column('attribute_id', alchemy_uuid, ForeignKey('user_attributes.id'), primary_key=True),
)

user_job_association = Table(
    'user_job_association', Base.metadata,
    Column('user_id', alchemy_uuid, ForeignKey('users.id'), primary_key=True),
          Column('job_id', alchemy_uuid, ForeignKey('jobs.id'), primary_key=True),
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
    notifications: Mapped[List["UserAttribute"]] = relationship(back_populates="user_id")
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
    location: Mapped[UUID] = mapped_column(ForeignKey('places.id'))
    is_active: Mapped[bool] = mapped_column(Boolean)
    organization_id: Mapped[UUID] = mapped_column(ForeignKey('organizations.id'))
    job_address: Mapped[str] = mapped_column(String(200))
    responded_users: Mapped[List["User"]] = relationship('User', secondary=user_job_association, back_populates='assigned_jobs')