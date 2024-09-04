from datetime import datetime
from typing import List
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Enum, String, func, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base
from src.models import Place
from src.models.ActionType import ActionType
from src.models.Organization import Organization
from src.schemas.JobSchema import JobStatusSchema, JobTypeSchema

if TYPE_CHECKING:
    from src.models.User import User


class Job(Base):
    __tablename__ = "jobs"
    id: Mapped[UUID] = mapped_column(primary_key=True)
    status_value: Mapped[str] = mapped_column(Enum(JobStatusSchema), index=True)
    type_value: Mapped[str] = mapped_column(Enum(JobTypeSchema), index=True)
    price: Mapped[int]
    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(400))
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.now(),
    )
    started_at: Mapped[datetime] = mapped_column(DateTime)
    finished_at: Mapped[datetime] = mapped_column(DateTime)
    action_type_id: Mapped[UUID] = mapped_column(ForeignKey("action_types.id"))
    city_id: Mapped[UUID] = mapped_column(ForeignKey("places.id"), index=True)
    job_location: Mapped[str] = mapped_column(String(400))
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        index=True,
    )
    organization_id: Mapped[UUID] = mapped_column(ForeignKey("organizations.id"))
    owner_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id"), index=True, nullable=False
    )

    responded_users: Mapped[List["User"]] = relationship(
        "User",
        secondary="user_job_association",
        back_populates="assigned_jobs",
        cascade="all, delete",
    )
    owner: Mapped["User"] = relationship(back_populates="created_jobs")
    organization: Mapped["Organization"] = relationship()
    action_type: Mapped["ActionType"] = relationship()
    city: Mapped["Place"] = relationship()
