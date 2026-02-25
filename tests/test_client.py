"""Test cases for the DataForSEO HTTP client functionality."""

import base64
import json
import os
import sys
import unittest
from unittest.mock import patch, MagicMock, call

# Ensure project root on path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tests.conftest import (
    MockHTTPResponse,
    EnvVarMixin,
    make_ai_response,
    make_full_response,
    patch_urlopen,
)


class TestAuthEncoding(unittest.TestCase):
    """Test that auth encoding matches btoa() behavior."""

    def test_basic_auth_encoding(self):
        from scripts.dataforseo import build_auth_header

        header = build_auth_header("user", "pass")
        expected_token = base64.b64encode(b"user:pass").decode()
        self.assertEqual(header, f"Basic {expected_token}")

    def test_auth_encoding_special_chars(self):
        from scripts.dataforseo import build_auth_header

        header = build_auth_header("user@example.com", "p@ss:w0rd!")
        expected_token = base64.b64encode(b"user@example.com:p@ss:w0rd!").decode()
        self.assertEqual(header, f"Basic {expected_token}")

    def test_auth_encoding_empty_password(self):
        from scripts.dataforseo import build_auth_header

        header = build_auth_header("user", "")
        expected_token = base64.b64encode(b"user:").decode()
        self.assertEqual(header, f"Basic {expected_token}")


class TestURLBuilding(unittest.TestCase):
    """Test URL construction with .ai suffix logic."""

    def test_ai_suffix_added_when_not_full_response_and_not_force_full(self):
        from scripts.dataforseo import build_url

        url = build_url("/v3/serp/google/organic/live/advanced", full_response=False, force_full=False)
        self.assertEqual(url, "https://api.dataforseo.com/v3/serp/google/organic/live/advanced.ai")

    def test_no_ai_suffix_when_full_response_true_and_force_full_false(self):
        from scripts.dataforseo import build_url

        url = build_url("/v3/serp/google/organic/live/advanced", full_response=True, force_full=False)
        self.assertEqual(url, "https://api.dataforseo.com/v3/serp/google/organic/live/advanced")

    def test_no_ai_suffix_when_full_response_false_and_force_full_true(self):
        from scripts.dataforseo import build_url

        url = build_url("/v3/serp/google/organic/live/advanced", full_response=False, force_full=True)
        self.assertEqual(url, "https://api.dataforseo.com/v3/serp/google/organic/live/advanced")

    def test_no_ai_suffix_when_full_response_true_and_force_full_true(self):
        from scripts.dataforseo import build_url

        url = build_url("/v3/serp/google/organic/live/advanced", full_response=True, force_full=True)
        self.assertEqual(url, "https://api.dataforseo.com/v3/serp/google/organic/live/advanced")

    def test_base_url_default(self):
        from scripts.dataforseo import build_url

        url = build_url("/v3/test", full_response=False, force_full=False)
        self.assertTrue(url.startswith("https://api.dataforseo.com"))


class TestRequestHeaders(unittest.TestCase):
    """Test that request headers are correctly set."""

    def test_request_includes_auth_and_content_type(self):
        from scripts.dataforseo import make_request

        mock_response = MockHTTPResponse(make_ai_response())
        with patch("urllib.request.urlopen", return_value=mock_response) as mock_urlopen:
            make_request(
                endpoint="/v3/test",
                method="POST",
                body=None,
                full_response=False,
                force_full=False,
                username="user",
                password="pass",
            )
            request_obj = mock_urlopen.call_args[0][0]
            self.assertIn("Authorization", request_obj.headers)
            self.assertIn("Content-type", request_obj.headers)
            expected_token = base64.b64encode(b"user:pass").decode()
            self.assertEqual(request_obj.headers["Authorization"], f"Basic {expected_token}")
            self.assertEqual(request_obj.headers["Content-type"], "application/json")


class TestPOSTBodyWrapping(unittest.TestCase):
    """Test POST body auto-wrapping in [{...}]."""

    def test_post_body_auto_wrapped_in_array(self):
        from scripts.dataforseo import make_request

        mock_response = MockHTTPResponse(make_ai_response())
        with patch("urllib.request.urlopen", return_value=mock_response) as mock_urlopen:
            make_request(
                endpoint="/v3/test",
                method="POST",
                body={"keyword": "seo"},
                full_response=False,
                force_full=False,
                username="user",
                password="pass",
                wrap_array=True,
            )
            request_obj = mock_urlopen.call_args[0][0]
            sent_body = json.loads(request_obj.data.decode("utf-8"))
            self.assertIsInstance(sent_body, list)
            self.assertEqual(len(sent_body), 1)
            self.assertEqual(sent_body[0], {"keyword": "seo"})

    def test_no_wrap_array_disables_wrapping(self):
        from scripts.dataforseo import make_request

        mock_response = MockHTTPResponse(make_ai_response())
        with patch("urllib.request.urlopen", return_value=mock_response) as mock_urlopen:
            make_request(
                endpoint="/v3/test",
                method="POST",
                body={"keyword": "seo"},
                full_response=False,
                force_full=False,
                username="user",
                password="pass",
                wrap_array=False,
            )
            request_obj = mock_urlopen.call_args[0][0]
            sent_body = json.loads(request_obj.data.decode("utf-8"))
            self.assertIsInstance(sent_body, dict)
            self.assertEqual(sent_body, {"keyword": "seo"})


class TestErrorHandling(unittest.TestCase):
    """Test error handling in the client."""

    def test_network_error_produces_json_error(self):
        from scripts.dataforseo import make_request
        import urllib.error

        with patch(
            "urllib.request.urlopen",
            side_effect=urllib.error.URLError("Connection refused"),
        ):
            result = make_request(
                endpoint="/v3/test",
                method="POST",
                body=None,
                full_response=False,
                force_full=False,
                username="user",
                password="pass",
            )
            self.assertEqual(result["status"], "error")
            self.assertIn("message", result)

    def test_http_error_produces_json_error(self):
        from scripts.dataforseo import make_request
        import urllib.error

        with patch(
            "urllib.request.urlopen",
            side_effect=urllib.error.HTTPError(
                url="https://api.dataforseo.com/v3/test",
                code=403,
                msg="Forbidden",
                hdrs={},
                fp=None,
            ),
        ):
            result = make_request(
                endpoint="/v3/test",
                method="POST",
                body=None,
                full_response=False,
                force_full=False,
                username="user",
                password="pass",
            )
            self.assertEqual(result["status"], "error")
            self.assertIn("message", result)


if __name__ == "__main__":
    unittest.main()
