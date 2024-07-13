from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey, String, Table, Column, DateTime, Boolean, LargeBinary
from sqlalchemy.dialects.postgresql import UUID as alchemy_uuid
from uuid import UUID
from typing import List

from src.database import Base

user_attribute_association = Table(
    'user_attribute_association', Base.metadata,
    Column('user_id', alchemy_uuid, ForeignKey('users.id')),
    Column('attribute_id', alchemy_uuid, ForeignKey('user_attributes.id'))
)

user_job_association = Table(
    'user_job_association', Base.metadata,
    Column('user_id', alchemy_uuid, ForeignKey('users.id')),
          Column('job_id', alchemy_uuid, ForeignKey('jobs.id'))
)

class User(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    attributes: Mapped[List["UserAttribute"]] = relationship("UserAttribute", secondary=user_attribute_association, back_populates='user' )
    full_name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50))
    hashed_password: Mapped[bytes] = mapped_column(LargeBinary)
    assigned_jobs: Mapped[List["Job"]] = relationship("Job", secondary=user_job_association, back_populates='responded_users')


class UserAttribute(Base):
    __tablename__ = 'user_attributes'

    id: Mapped[UUID] = mapped_column(primary_key=True)
    key: Mapped[str] = mapped_column(String(50), nullable=False)
    value : Mapped[str] = mapped_column(String(50), nullable=False)

    user = relationship('User', secondary=user_attribute_association, back_populates='attributes')


class Job(Base):
    __tablename__ = 'jobs'
    id : Mapped[UUID] = mapped_column(primary_key=True)
    title : Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(400))
    period: Mapped[DateTime] = mapped_column(DateTime)
    action_type: Mapped[UUID] = mapped_column(ForeignKey('action_types.id'))
    location: Mapped[UUID] = mapped_column(ForeignKey('places.id'))
    is_active: Mapped[bool] = mapped_column(Boolean)

    responded_users: Mapped[List["User"]] = relationship('User', secondary=user_job_association, back_populates='assigned_jobs')