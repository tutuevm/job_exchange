from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID as sqlalchemy_uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import UUID
from typing import List

from src.database import Base

