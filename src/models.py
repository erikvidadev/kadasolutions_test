from datetime import datetime
from enum import Enum

from sqlalchemy import Enum as SQLEnum, Column, Integer, String, DateTime

from database import Base


class StatusEnum(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    description = Column(String, index=True)
    created_date = Column(DateTime, default=datetime.now)
    due_date = Column(DateTime)
    status = Column(SQLEnum(StatusEnum), default=StatusEnum.pending)
