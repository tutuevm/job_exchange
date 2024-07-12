from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey, String, Table, Column
from sqlalchemy.dialects.postgresql import UUID as alchemy_uuid
from uuid import UUID
from typing import List

from src.database import Base

user_attribute_association = Table(
    'user_attribute_association', Base.metadata,
    Column('user_id', alchemy_uuid, ForeignKey('user.id')),
    Column('attribute_id', alchemy_uuid, ForeignKey('attributes.id'))
)

class User(Base):
    __tablename__ = "user"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    attributes: Mapped[List["UserAttribute"]] = relationship("UserAttribute", secondary=user_attribute_association, back_populates='user' )
    full_name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50))
    hashed_password: Mapped[str] = mapped_column(String(128))
    assigned_jobs = relationship("JobResponse", back_populates='user')


class UserAttribute(Base):
    __tablename__ = 'user_attribute'

    id: Mapped[UUID] = mapped_column(primary_key=True)
    key = Column(String, nullable=False)
    value = Column(String, nullable=False)

    user = relationship('User', secondary=user_attribute_association, back_populates='attributes')