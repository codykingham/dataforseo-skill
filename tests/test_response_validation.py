"""Test cases for response validation (AI-condensed and full response)."""

import os
import sys
import unittest

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


class TestAIResponseValidation(unittest.TestCase):
    """Test AI-condensed response validation."""

    def test_valid_ai_response_20000(self):
        """status_code 20000 / 100 = 200, which is in 2xx range => valid."""
        from scripts.dataforseo import validate_ai_response

        response = {
            "id": "test",
            "status_code": 20000,
            "status_message": "Ok.",
            "items": [],
        }
        # Should not raise
        result = validate_ai_response(response)
        self.assertTrue(result)

    def test_invalid_ai_response_20100(self):
        """status_code 20100 / 100 = 201, which != 200 => invalid (matches TS)."""
        from scripts.dataforseo import validate_ai_response

        response = {
            "id": "test",
            "status_code": 20100,
            "status_message": "Created.",
            "items": [],
        }
        with self.assertRaises(Exception):
            validate_ai_response(response)

    def test_invalid_ai_response_40000(self):
        """status_code 40000 / 100 = 400, not in 2xx range => invalid."""
        from scripts.dataforseo import validate_ai_response

        response = {
            "id": "test",
            "status_code": 40000,
            "status_message": "Bad Request.",
            "items": [],
        }
        with self.assertRaises(Exception):
            validate_ai_response(response)

    def test_invalid_ai_response_50000(self):
        """status_code 50000 / 100 = 500, not in 2xx range => invalid."""
        from scripts.dataforseo import validate_ai_response

        response = {
            "id": "test",
            "status_code": 50000,
            "status_message": "Internal Error.",
            "items": [],
        }
        with self.assertRaises(Exception):
            validate_ai_response(response)


class TestFullResponseValidation(unittest.TestCase):
    """Test full response validation."""

    def test_valid_full_response(self):
        """Outer status OK, tasks non-empty, first task OK, tasks_error=0."""
        from scripts.dataforseo import validate_full_response

        response = {
            "version": "0.1",
            "status_code": 20000,
            "status_message": "Ok.",
            "time": "0.1s",
            "cost": 0.001,
            "tasks_count": 1,
            "tasks_error": 0,
            "tasks": [
                {
                    "id": "task-1",
                    "status_code": 20000,
                    "status_message": "Ok.",
                    "time": "0.1s",
                    "cost": 0.001,
                    "result_count": 1,
                    "path": [],
                    "data": {},
                    "result": [{"data": "value"}],
                }
            ],
        }
        result = validate_full_response(response)
        self.assertTrue(result)

    def test_invalid_outer_status(self):
        """Outer status_code is bad."""
        from scripts.dataforseo import validate_full_response

        response = {
            "version": "0.1",
            "status_code": 40000,
            "status_message": "Bad Request.",
            "time": "0.1s",
            "cost": 0,
            "tasks_count": 0,
            "tasks_error": 0,
            "tasks": [],
        }
        with self.assertRaises(Exception):
            validate_full_response(response)

    def test_invalid_empty_tasks(self):
        """Tasks list is empty."""
        from scripts.dataforseo import validate_full_response

        response = {
            "version": "0.1",
            "status_code": 20000,
            "status_message": "Ok.",
            "time": "0.1s",
            "cost": 0,
            "tasks_count": 0,
            "tasks_error": 0,
            "tasks": [],
        }
        with self.assertRaises(Exception):
            validate_full_response(response)

    def test_invalid_first_task_error_status(self):
        """First task has non-2xx status code."""
        from scripts.dataforseo import validate_full_response

        response = {
            "version": "0.1",
            "status_code": 20000,
            "status_message": "Ok.",
            "time": "0.1s",
            "cost": 0,
            "tasks_count": 1,
            "tasks_error": 0,
            "tasks": [
                {
                    "id": "task-1",
                    "status_code": 40000,
                    "status_message": "Task Error.",
                    "time": "0.1s",
                    "cost": 0,
                    "result_count": 0,
                    "path": [],
                    "data": {},
                    "result": [],
                }
            ],
        }
        with self.assertRaises(Exception):
            validate_full_response(response)

    def test_invalid_tasks_error_count(self):
        """tasks_error > 0."""
        from scripts.dataforseo import validate_full_response

        response = {
            "version": "0.1",
            "status_code": 20000,
            "status_message": "Ok.",
            "time": "0.1s",
            "cost": 0,
            "tasks_count": 1,
            "tasks_error": 2,
            "tasks": [
                {
                    "id": "task-1",
                    "status_code": 20000,
                    "status_message": "Ok.",
                    "time": "0.1s",
                    "cost": 0,
                    "result_count": 0,
                    "path": [],
                    "data": {},
                    "result": [],
                }
            ],
        }
        with self.assertRaises(Exception):
            validate_full_response(response)


if __name__ == "__main__":
    unittest.main()
