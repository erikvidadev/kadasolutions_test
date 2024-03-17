from datetime import datetime
from enum import Enum

from sqlalchemy import Enum as SQLEnum, Column, Integer, String, DateTime

from src.database import Base


class StatusEnum(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    created_date = Column(DateTime, default=datetime.now)
    due_date = Column(DateTime)
    status = Column(SQLEnum(StatusEnum), default=StatusEnum.PENDING)
