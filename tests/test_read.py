import unittest
from unittest.mock import MagicMock

from sqlalchemy.orm import Session

import src.crud as crud
import src.models as models


class TestGetTaskById(unittest.TestCase):
    def setUp(self):
        self.mock_db = MagicMock(spec=Session)

    def test_get_task_by_id_existing_task(self):
        expected_task = models.Task(id=1, title="Test Task", description="Test Description")
        self.mock_db.query().filter().first.return_value = expected_task

        result = crud.get_task_by_id(self.mock_db, task_id=1)

        self.assertEqual(result, expected_task)

    def test_get_task_by_id_non_existing_task(self):
        self.mock_db.query().filter().first.return_value = None

        result = crud.get_task_by_id(self.mock_db, task_id=1)

        self.assertIsNone(result)


class TestGetTasks(unittest.TestCase):
    def setUp(self):
        self.mock_db = MagicMock(spec=Session)

    def test_get_tasks_with_results(self):
        expected_tasks = [
            models.Task(id=1, title="Task 1", description="Description 1"),
            models.Task(id=2, title="Task 2", description="Description 2")
        ]
        self.mock_db.query().all.return_value = expected_tasks

        result = crud.get_tasks(self.mock_db)

        self.assertEqual(result, expected_tasks)

    def test_get_tasks_no_results(self):
        self.mock_db.query().all.return_value = []

        result = crud.get_tasks(self.mock_db)

        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
