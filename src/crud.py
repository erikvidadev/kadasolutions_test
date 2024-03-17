from typing import Optional

from sqlalchemy import asc, desc
from sqlalchemy.orm import Session

from src import models, schemas


def get_task_by_id(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()


def get_task_by_title(db: Session, task_title: str):
    return db.query(models.Task).filter(models.Task.title == task_title).first()


def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Task).offset(skip).limit(limit).all()


def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(
        title=task.title,
        description=task.description,
        due_date=task.due_date,
        status=task.status
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def update_task(db: Session, task_id: int, task: schemas.TaskCreate):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task:
        for key, value in task.dict().items():
            setattr(db_task, key, value)
        db.commit()
        db.refresh(db_task)
        return db_task
    else:
        return None


def delete_task(db: Session, task_id: int):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task:
        db.delete(db_task)
        db.commit()
        return True
    else:
        return False


def filter_and_sort_tasks(db: Session,
                          status: Optional[str] = None,
                          sort_by: Optional[str] = None,
                          order: Optional[str] = None,
                          skip: int = 0,
                          limit: int = 100):
    query = db.query(models.Task)
    if status:
        query = query.filter(models.Task.status == status)

    if sort_by:
        if order == "asc":
            query = query.order_by(asc(getattr(models.Task, sort_by)))
        elif order == "desc":
            query = query.order_by(desc(getattr(models.Task, sort_by)))

    query = query.offset(skip).limit(limit)
    return query.all()
