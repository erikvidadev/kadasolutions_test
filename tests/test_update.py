import unittest
from unittest.mock import MagicMock

from sqlalchemy.orm import Session

import src.crud as crud
import src.models as models
import src.schemas as schemas


class TestUpdateTask(unittest.TestCase):

    def setUp(self):
        self.mock_db = MagicMock(spec=Session)

    def test_update_existing_task(self):
        existing_task_id = 1
        existing_task = models.Task(id=existing_task_id, title="Old Title", description="Old Description")
        updated_task_data = {"title": "Updated Title", "description": "Updated Description"}
        updated_task_schema = schemas.TaskCreate(**updated_task_data)

        self.mock_db.query().filter().first.return_value = existing_task

        self.mock_db.commit.return_value = None
        self.mock_db.refresh.return_value = None

        updated_task = crud.update_task(self.mock_db, task_id=existing_task_id, task=updated_task_schema)

        self.assertEqual(updated_task.title, updated_task_data["title"])
        self.assertEqual(updated_task.description, updated_task_data["description"])

    def test_update_non_existing_task(self):
        non_existing_task_id = 1
        self.mock_db.query().filter().first.return_value = None

        result = crud.update_task(self.mock_db, task_id=non_existing_task_id, task=None)

        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
