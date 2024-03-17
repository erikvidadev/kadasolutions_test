import unittest
from unittest.mock import MagicMock
from sqlalchemy.orm import Session
from src import crud, models


class TestFilterAndSortTasks(unittest.TestCase):
    def test_filter_and_sort_tasks(self):
        mock_db_session = MagicMock(spec=Session)

        mock_tasks = [
            models.Task(id=1, title="Task 1", status="pending", created_date="2022-01-01", due_date="2022-01-05"),
            models.Task(id=2, title="Task 2", status="completed", created_date="2022-01-02", due_date="2022-01-06"),
            models.Task(id=3, title="Task 3", status="in_progress", created_date="2022-01-03", due_date="2022-01-07"),
        ]

        mock_db_session.query().filter().order_by().limit().all.return_value = mock_tasks

        result = crud.filter_and_sort_tasks(
            db=mock_db_session,
            status="pending",
            sort_by="created_date",
            order="asc",
            limit=100
        )

        self.assertEqual(result, mock_tasks)


if __name__ == '__main__':
    unittest.main()
