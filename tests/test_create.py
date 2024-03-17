import datetime
from unittest.mock import MagicMock


from src import schemas, crud

mock_db = MagicMock()

task_data = schemas.TaskCreate(
    title="Test Task",
    description="Test Description",
    due_date=datetime.datetime(2008, 5, 23),
    status="pending"
)


def test_create_task():
    created_task = crud.create_task(db=mock_db, task=task_data)

    assert created_task.title == "Test Task"
    assert created_task.description == "Test Description"
    assert created_task.due_date == datetime.datetime(2008, 5, 23)
    assert created_task.status == "pending"
