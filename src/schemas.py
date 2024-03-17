from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class StatusEnum(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    status: StatusEnum = StatusEnum.pending


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    pass


class TaskInDB(TaskBase):
    id: int
    created_date: datetime

    class Config:
        orm_mode = True  #Pydantic's orm_mode will tell the Pydantic model to read the data even if it is not a dict,
                         #but an ORM model (or any other arbitrary object with attributes).
