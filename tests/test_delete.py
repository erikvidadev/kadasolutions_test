import unittest
from unittest.mock import MagicMock

from sqlalchemy.orm import Session

import src.crud as crud
import src.models as models


class TestDeleteTask(unittest.TestCase):

    def setUp(self):
        self.mock_db = MagicMock(spec=Session)

    def test_delete_existing_task(self):
        existing_task_id = 1
        existing_task = models.Task(id=existing_task_id, title="Test Task", description="Test Description")

        self.mock_db.query().filter().first.return_value = existing_task

        self.mock_db.delete.return_value = None
        self.mock_db.commit.return_value = None

        result = crud.delete_task(self.mock_db, task_id=existing_task_id)

        self.assertTrue(result)

    def test_delete_non_existing_task(self):
        non_existing_task_id = 1
        self.mock_db.query().filter().first.return_value = None

        result = crud.delete_task(self.mock_db, task_id=non_existing_task_id)

        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()