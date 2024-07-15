from sqlalchemy import String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import UUID
from typing import List, TYPE_CHECKING

from src.database import Base

if TYPE_CHECKING:
    from src.models.User import user_job_association

