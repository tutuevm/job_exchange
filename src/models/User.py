from typing import List
from uuid import UUID

from sqlalchemy import (
    ForeignKey,
    String,
    Table,
    Column,
    LargeBinary,
    Enum,
)
from sqlalchemy.dialects.postgresql import UUID as alchemy_uuid
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database import Base
from src.models.Job import Job
from src.models.Notifications import Notification
from src.models.Transaction import Transaction
from src.schemas.JobResponseType import JobResponseType

user_attribute_association = Table(
    "user_attribute_association",
    Base.metadata,
    Column("user_id", alchemy_uuid, ForeignKey("users.id"), primary_key=True),
    Column(
        "attribute_id", alchemy_uuid, ForeignKey("user_attributes.id"), primary_key=True
    ),
)

user_job_association = Table(
    "user_job_association",
    Base.metadata,
    Column(
        "user_id",
        alchemy_uuid,
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column(
        "job_id",
        alchemy_uuid,
        ForeignKey("jobs.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column(
        "response_status",
        Enum(JobResponseType),
        default=JobResponseType.SUBMITTED,
        nullable=False,
    ),
)


class User(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(String(50))
    login: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    email: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    hashed_password: Mapped[bytes] = mapped_column(LargeBinary)
    is_active: Mapped[bool] = mapped_column(default=True)

    notifications: Mapped[List["Notification"]] = relationship(back_populates="user")
    attributes: Mapped[List["UserAttribute"]] = relationship(
        "UserAttribute", secondary=user_attribute_association, back_populates="user"
    )
    created_jobs: Mapped[List["Job"]] = relationship(back_populates="owner")
    assigned_jobs: Mapped[List["Job"]] = relationship(
        "Job",
        secondary=user_job_association,
        back_populates="responded_users",
        cascade="all, delete",
    )
    transactions_list: Mapped[List["Transaction"]] = relationship()


class UserAttribute(Base):
    __tablename__ = "user_attributes"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    key: Mapped[str] = mapped_column(String(50), nullable=False)
    value: Mapped[str] = mapped_column(String(50), nullable=False)

    user = relationship(
        "User", secondary=user_attribute_association, back_populates="attributes"
    )
