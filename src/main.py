from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy.orm import Session

from src import models, schemas, crud
from src.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/tasks/", response_model=schemas.TaskBase)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    """
    You can create here your tasks.
    """
    existing_task = crud.get_task_by_title(db, task_title=task.title)
    if existing_task:
        raise HTTPException(status_code=400, detail="A task with this title already exists")
    return crud.create_task(db=db, task=task)


@app.get("/tasks/", response_model=List[schemas.TaskBase])
def read_tasks(db: Session = Depends(get_db)):
    """
    You can read all of your task from the database.
    """
    tasks = crud.get_tasks(db)
    return tasks


@app.get("/tasks/{task_id}", response_model=schemas.TaskBase)
def read_task_by_id(task_id: int, db: Session = Depends(get_db)):
    """
    You can read a task from the database here by its id.
    """
    db_task = crud.get_task_by_id(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task


@app.put("/tasks/{task_id}", response_model=schemas.TaskBase)
def update_task(task_id: int, task: schemas.TaskCreate, db: Session = Depends(get_db)):
    """
    You can update any argument of your task by its id.
    """
    updated_task = crud.update_task(db, task_id, task)
    if updated_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task


@app.delete("/tasks/{task_id}", response_model=bool)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    """
    You can delete here any of your tasks by its id.
    """
    result = crud.delete_task(db, task_id)
    if not result:
        raise HTTPException(status_code=404, detail="Task not found")
    return True


@app.get("/filtered-tasks/", response_model=List[schemas.TaskBase])
def filter_and_sort_tasks(

        status: Optional[str] = Query(None, description="Filter tasks by status.(pending, in_progress, completed)"),
        sort_by: Optional[str] = Query(None, description="Field to sort tasks by (created_date or due_date)"),
        order: Optional[str] = Query(None, description="Sort order (asc or desc)"),
        limit: int = Query(100, description="Maximum number of items to return"),
        db: Session = Depends(get_db)
):
    """
    You can fileter and sort your task here and list them in the required quantity .
    """
    valid_sort_fields = [None, "created_date", "due_date"]
    valid_sort_orders = [None, "asc", "desc"]
    valid_statuses = [None, "pending", "in_progress", "completed"]

    if sort_by not in valid_sort_fields:
        raise HTTPException(status_code=400,
                            detail="Invalid value for sort_by parameter. It should be 'created_date' or 'due_date'.")

    if order not in valid_sort_orders:
        raise HTTPException(status_code=400,
                            detail="Invalid value for order parameter. It should be 'asc' or 'desc'.")

    if status not in valid_statuses:
        raise HTTPException(status_code=400,
                            detail="Invalid value for status parameter. "
                                   "It should be 'pending', 'in_progress', or 'completed'.")

    return crud.filter_and_sort_tasks(db, status=status, sort_by=sort_by, order=order, limit=limit)
