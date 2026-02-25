"""Shared fixtures and mock HTTP helpers for DataForSEO client tests."""

import io
import json
import os
import sys
import unittest
from unittest.mock import MagicMock, patch

# Ensure the project root is on sys.path so `scripts.dataforseo` is importable
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


class MockHTTPResponse:
    """Mock urllib HTTP response object."""

    def __init__(self, data, status_code=200, headers=None):
        if isinstance(data, str):
            self._body = data.encode("utf-8")
        elif isinstance(data, bytes):
            self._body = data
        else:
            self._body = json.dumps(data).encode("utf-8")
        self.status = status_code
        self.headers = headers or {}
        self._stream = io.BytesIO(self._body)

    def read(self):
        return self._body

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass


def make_ai_response(status_code=20000, status_message="Ok.", items=None):
    """Create a mock AI-condensed response structure."""
    return {
        "id": "test-id-123",
        "status_code": status_code,
        "status_message": status_message,
        "items": items or [],
    }


def make_full_response(
    status_code=20000,
    status_message="Ok.",
    tasks_error=0,
    tasks=None,
):
    """Create a mock full API response structure."""
    if tasks is None:
        tasks = [
            {
                "id": "task-1",
                "status_code": 20000,
                "status_message": "Ok.",
                "time": "0.1s",
                "cost": 0.001,
                "result_count": 1,
                "path": [],
                "data": {},
                "result": [{"some": "data"}],
            }
        ]
    return {
        "version": "0.1",
        "status_code": status_code,
        "status_message": status_message,
        "time": "0.1s",
        "cost": 0.001,
        "tasks_count": len(tasks),
        "tasks_error": tasks_error,
        "tasks": tasks,
    }


class EnvVarMixin:
    """Mixin for setting/clearing environment variables in tests."""

    _original_env: dict

    def set_env(self, **kwargs):
        """Set environment variables, saving originals for later restore."""
        if not hasattr(self, "_original_env"):
            self._original_env = {}
        for key, value in kwargs.items():
            if key not in self._original_env:
                self._original_env[key] = os.environ.get(key)
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value

    def restore_env(self):
        """Restore all modified environment variables."""
        if hasattr(self, "_original_env"):
            for key, value in self._original_env.items():
                if value is None:
                    os.environ.pop(key, None)
                else:
                    os.environ[key] = value
            self._original_env = {}


def patch_urlopen(response_data, status_code=200):
    """Return a patch context manager for urllib.request.urlopen."""
    mock_resp = MockHTTPResponse(response_data, status_code)
    return patch("urllib.request.urlopen", return_value=mock_resp)
