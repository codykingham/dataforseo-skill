"""Test cases for dot-notation field filtering with wildcard support."""

import os
import sys
import unittest

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL_DIR = os.path.join(PROJECT_ROOT, "dataforseo")
for _p in (PROJECT_ROOT, SKILL_DIR):
    if _p not in sys.path:
        sys.path.insert(0, _p)


class TestSimpleDotPaths(unittest.TestCase):
    """Test simple dot-notation path extraction."""

    def test_extract_nested_value(self):
        from scripts.dataforseo import filter_fields

        data = {"items": {"url": "https://example.com", "title": "Example"}}
        result = filter_fields(data, "items.url")
        self.assertIn("items", result)
        self.assertEqual(result["items"]["url"], "https://example.com")
        # title should not be in result
        self.assertNotIn("title", result.get("items", {}))

    def test_extract_top_level_field(self):
        from scripts.dataforseo import filter_fields

        data = {"name": "test", "value": 42}
        result = filter_fields(data, "name")
        self.assertEqual(result["name"], "test")
        self.assertNotIn("value", result)


class TestWildcardAtEnd(unittest.TestCase):
    """Test wildcard at end of path."""

    def test_wildcard_gets_all_fields_of_object(self):
        from scripts.dataforseo import filter_fields

        data = {"items": {"url": "https://example.com", "title": "Example", "rank": 1}}
        result = filter_fields(data, "items.*")
        self.assertEqual(result["items"]["url"], "https://example.com")
        self.assertEqual(result["items"]["title"], "Example")
        self.assertEqual(result["items"]["rank"], 1)


class TestWildcardInMiddle(unittest.TestCase):
    """Test wildcard in middle of path for array items."""

    def test_wildcard_extracts_field_from_all_array_items(self):
        from scripts.dataforseo import filter_fields

        data = {
            "items": [
                {"backlinks": 100, "rank": 1, "url": "a.com"},
                {"backlinks": 200, "rank": 2, "url": "b.com"},
            ]
        }
        result = filter_fields(data, "items.*.backlinks")
        self.assertEqual(len(result["items"]), 2)
        self.assertEqual(result["items"][0]["backlinks"], 100)
        self.assertEqual(result["items"][1]["backlinks"], 200)
        # Other fields should not be present
        self.assertNotIn("rank", result["items"][0])

    def test_wildcard_middle_with_object(self):
        from scripts.dataforseo import filter_fields

        data = {
            "results": {
                "a": {"score": 10, "name": "first"},
                "b": {"score": 20, "name": "second"},
            }
        }
        result = filter_fields(data, "results.*.score")
        self.assertEqual(result["results"]["a"]["score"], 10)
        self.assertEqual(result["results"]["b"]["score"], 20)


class TestArrayBracketNotation(unittest.TestCase):
    """Test array bracket notation in field paths."""

    def test_bracket_notation(self):
        from scripts.dataforseo import filter_fields

        data = {"items": ["first", "second", "third"]}
        result = filter_fields(data, "items[0]")
        self.assertIn("items", result)


class TestMultipleFields(unittest.TestCase):
    """Test comma-separated multiple fields."""

    def test_multiple_fields_comma_separated(self):
        from scripts.dataforseo import filter_fields

        data = {
            "items": [
                {"backlinks": 100, "rank": 1, "url": "a.com"},
                {"backlinks": 200, "rank": 2, "url": "b.com"},
            ]
        }
        result = filter_fields(data, "items.*.backlinks,items.*.rank")
        self.assertEqual(result["items"][0]["backlinks"], 100)
        self.assertEqual(result["items"][0]["rank"], 1)
        self.assertNotIn("url", result["items"][0])

    def test_multiple_top_level_fields(self):
        from scripts.dataforseo import filter_fields

        data = {"name": "test", "value": 42, "extra": "drop"}
        result = filter_fields(data, "name,value")
        self.assertEqual(result["name"], "test")
        self.assertEqual(result["value"], 42)
        self.assertNotIn("extra", result)


class TestEdgeCases(unittest.TestCase):
    """Test edge cases for field filtering."""

    def test_null_values_do_not_crash(self):
        from scripts.dataforseo import filter_fields

        data = {"items": None}
        result = filter_fields(data, "items.url")
        # Should not crash; result should not have items.url
        self.assertIsInstance(result, dict)

    def test_empty_object(self):
        from scripts.dataforseo import filter_fields

        data = {}
        result = filter_fields(data, "items.url")
        self.assertIsInstance(result, dict)

    def test_missing_key_does_not_crash(self):
        from scripts.dataforseo import filter_fields

        data = {"other": "value"}
        result = filter_fields(data, "items.url")
        self.assertIsInstance(result, dict)
        self.assertNotIn("items", result)

    def test_none_data_returns_none(self):
        from scripts.dataforseo import filter_fields

        result = filter_fields(None, "items.url")
        self.assertIsNone(result)

    def test_empty_field_spec_returns_data(self):
        from scripts.dataforseo import filter_fields

        data = {"name": "test"}
        result = filter_fields(data, "")
        self.assertEqual(result, data)

    def test_nested_objects(self):
        from scripts.dataforseo import filter_fields

        data = {
            "level1": {
                "level2": {
                    "level3": {"target": "found", "noise": "skip"}
                }
            }
        }
        result = filter_fields(data, "level1.level2.level3.target")
        self.assertEqual(result["level1"]["level2"]["level3"]["target"], "found")
        self.assertNotIn("noise", result["level1"]["level2"]["level3"])


if __name__ == "__main__":
    unittest.main()
