from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from uuid import UUID, uuid4

from src.database import Base


class JobStatus(Base):
    __tablename__ = 'job_status'

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    title: Mapped[str] = mapped_column(String(20))

