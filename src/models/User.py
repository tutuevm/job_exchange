from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey, String, Table, Column, DateTime
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
    hashed_password: Mapped[str] = mapped_column(String(128))
    assigned_jobs = relationship("JobResponse", back_populates='user')


class UserAttribute(Base):
    __tablename__ = 'user_attributes'

    id: Mapped[UUID] = mapped_column(primary_key=True)
    key = Column(String, nullable=False)
    value = Column(String, nullable=False)

    user = relationship('User', secondary=user_attribute_association, back_populates='attributes')


