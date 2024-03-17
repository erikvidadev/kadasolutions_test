from datetime import datetime

from sqlalchemy import Enum, Column, Integer, String, DateTime

from src.database import Base


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
    status = Column(Enum(StatusEnum), default=StatusEnum.pending)
