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

from src.Job.models import Job
from src.Job.schemas import JobResponseType
from src.ManagerData.models import ManagerData
from src.Notification.models import Notification
from src.Transaction.models import Transaction
from src.UserData.models import UserData
from src.database import Base

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
    login: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    email: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    hashed_password: Mapped[bytes] = mapped_column(LargeBinary)
    is_active: Mapped[bool] = mapped_column(default=True)
    full_name: Mapped[str] = mapped_column(nullable=True)

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
    user_data: Mapped["UserData"] = relationship(back_populates="user")
    manager_data: Mapped["ManagerData"] = relationship(back_populates="user")
