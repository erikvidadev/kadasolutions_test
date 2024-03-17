from datetime import datetime

from pydantic import BaseModel

from src.models import StatusEnum


class TaskBase(BaseModel):
    title: str
    description: str
    due_date: datetime = None
    status: StatusEnum = StatusEnum.PENDING


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    created_date: datetime

    class Config:
        orm_mode = True  # Pydantic's orm_mode will tell the Pydantic model to read the data even if it is not a dict,
        # but an ORM model (or any other arbitrary object with attributes).
