"""Test cases for configuration parsing from environment variables and field config."""

import json
import os
import sys
import tempfile
import unittest

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tests.conftest import EnvVarMixin


class TestEnvVarParsing(EnvVarMixin, unittest.TestCase):
    """Test env var parsing for username and password."""

    def setUp(self):
        self._original_env = {}

    def tearDown(self):
        self.restore_env()

    def test_username_from_env(self):
        from scripts.dataforseo import get_config

        self.set_env(DATAFORSEO_USERNAME="testuser", DATAFORSEO_PASSWORD="testpass")
        config = get_config()
        self.assertEqual(config["username"], "testuser")

    def test_password_from_env(self):
        from scripts.dataforseo import get_config

        self.set_env(DATAFORSEO_USERNAME="testuser", DATAFORSEO_PASSWORD="testpass")
        config = get_config()
        self.assertEqual(config["password"], "testpass")


class TestFullResponseEnvVar(EnvVarMixin, unittest.TestCase):
    """Test DATAFORSEO_FULL_RESPONSE env var parsing."""

    def setUp(self):
        self._original_env = {}

    def tearDown(self):
        self.restore_env()

    def test_full_response_true_string(self):
        from scripts.dataforseo import get_config

        self.set_env(
            DATAFORSEO_USERNAME="u",
            DATAFORSEO_PASSWORD="p",
            DATAFORSEO_FULL_RESPONSE="true",
        )
        config = get_config()
        self.assertTrue(config["full_response"])

    def test_full_response_false_string(self):
        from scripts.dataforseo import get_config

        self.set_env(
            DATAFORSEO_USERNAME="u",
            DATAFORSEO_PASSWORD="p",
            DATAFORSEO_FULL_RESPONSE="false",
        )
        config = get_config()
        self.assertFalse(config["full_response"])

    def test_full_response_1(self):
        from scripts.dataforseo import get_config

        self.set_env(
            DATAFORSEO_USERNAME="u",
            DATAFORSEO_PASSWORD="p",
            DATAFORSEO_FULL_RESPONSE="1",
        )
        config = get_config()
        self.assertTrue(config["full_response"])

    def test_full_response_0(self):
        from scripts.dataforseo import get_config

        self.set_env(
            DATAFORSEO_USERNAME="u",
            DATAFORSEO_PASSWORD="p",
            DATAFORSEO_FULL_RESPONSE="0",
        )
        config = get_config()
        self.assertFalse(config["full_response"])

    def test_full_response_unset_defaults_false(self):
        from scripts.dataforseo import get_config

        self.set_env(
            DATAFORSEO_USERNAME="u",
            DATAFORSEO_PASSWORD="p",
            DATAFORSEO_FULL_RESPONSE=None,
        )
        config = get_config()
        self.assertFalse(config["full_response"])


class TestSimpleFilterEnvVar(EnvVarMixin, unittest.TestCase):
    """Test DATAFORSEO_SIMPLE_FILTER env var parsing."""

    def setUp(self):
        self._original_env = {}

    def tearDown(self):
        self.restore_env()

    def test_simple_filter_true(self):
        from scripts.dataforseo import get_config

        self.set_env(
            DATAFORSEO_USERNAME="u",
            DATAFORSEO_PASSWORD="p",
            DATAFORSEO_SIMPLE_FILTER="true",
        )
        config = get_config()
        self.assertTrue(config["simple_filter"])

    def test_simple_filter_unset_defaults_false(self):
        from scripts.dataforseo import get_config

        self.set_env(
            DATAFORSEO_USERNAME="u",
            DATAFORSEO_PASSWORD="p",
            DATAFORSEO_SIMPLE_FILTER=None,
        )
        config = get_config()
        self.assertFalse(config["simple_filter"])


class TestDebugEnvVar(EnvVarMixin, unittest.TestCase):
    """Test DEBUG env var parsing."""

    def setUp(self):
        self._original_env = {}

    def tearDown(self):
        self.restore_env()

    def test_debug_true(self):
        from scripts.dataforseo import get_config

        self.set_env(
            DATAFORSEO_USERNAME="u",
            DATAFORSEO_PASSWORD="p",
            DEBUG="true",
        )
        config = get_config()
        self.assertTrue(config["debug"])

    def test_debug_unset_defaults_false(self):
        from scripts.dataforseo import get_config

        self.set_env(
            DATAFORSEO_USERNAME="u",
            DATAFORSEO_PASSWORD="p",
            DEBUG=None,
        )
        config = get_config()
        self.assertFalse(config["debug"])


class TestFieldConfigPath(EnvVarMixin, unittest.TestCase):
    """Test FIELD_CONFIG_PATH loading."""

    def setUp(self):
        self._original_env = {}

    def tearDown(self):
        self.restore_env()

    def test_load_field_config_from_file(self):
        from scripts.dataforseo import load_field_config

        config_data = {
            "supported_fields": {
                "test_tool": ["items.url", "items.title"]
            }
        }
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False
        ) as f:
            json.dump(config_data, f)
            tmp_path = f.name

        try:
            result = load_field_config(tmp_path)
            self.assertIsNotNone(result)
            self.assertIn("supported_fields", result)
            self.assertIn("test_tool", result["supported_fields"])
        finally:
            os.unlink(tmp_path)

    def test_load_field_config_missing_file(self):
        from scripts.dataforseo import load_field_config

        result = load_field_config("/nonexistent/path/config.json")
        self.assertIsNone(result)

    def test_query_field_config(self):
        from scripts.dataforseo import query_field_config

        config = {
            "supported_fields": {
                "test_tool": ["items.url", "items.title"]
            }
        }
        fields = query_field_config(config, "test_tool")
        self.assertEqual(fields, ["items.url", "items.title"])

    def test_query_field_config_missing_tool(self):
        from scripts.dataforseo import query_field_config

        config = {"supported_fields": {"other_tool": ["field1"]}}
        fields = query_field_config(config, "nonexistent_tool")
        self.assertIsNone(fields)

    def test_clear_field_config(self):
        from scripts.dataforseo import clear_field_config, load_field_config

        config_data = {"supported_fields": {"tool": ["field"]}}
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False
        ) as f:
            json.dump(config_data, f)
            tmp_path = f.name

        try:
            config = load_field_config(tmp_path)
            self.assertIsNotNone(config)
            cleared = clear_field_config()
            self.assertIsNone(cleared)
        finally:
            os.unlink(tmp_path)

    def test_invalid_config_format(self):
        from scripts.dataforseo import load_field_config

        config_data = {"not_supported_fields": {}}
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False
        ) as f:
            json.dump(config_data, f)
            tmp_path = f.name

        try:
            result = load_field_config(tmp_path)
            self.assertIsNone(result)
        finally:
            os.unlink(tmp_path)


if __name__ == "__main__":
    unittest.main()
