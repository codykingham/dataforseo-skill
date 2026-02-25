"""Test cases for utility functions."""

import os
import sys
import unittest

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


class TestMapArrayToNumberedKeys(unittest.TestCase):
    """Test map_array_to_numbered_keys utility function."""

    def test_basic_mapping(self):
        from scripts.dataforseo import map_array_to_numbered_keys

        result = map_array_to_numbered_keys(["a", "b"])
        self.assertEqual(result, {"1": "a", "2": "b"})

    def test_empty_array(self):
        from scripts.dataforseo import map_array_to_numbered_keys

        result = map_array_to_numbered_keys([])
        self.assertEqual(result, {})

    def test_single_item(self):
        from scripts.dataforseo import map_array_to_numbered_keys

        result = map_array_to_numbered_keys(["x"])
        self.assertEqual(result, {"1": "x"})

    def test_three_items(self):
        from scripts.dataforseo import map_array_to_numbered_keys

        result = map_array_to_numbered_keys(["val_1", "val_2", "val_3"])
        self.assertEqual(result, {"1": "val_1", "2": "val_2", "3": "val_3"})

    def test_keys_are_strings(self):
        from scripts.dataforseo import map_array_to_numbered_keys

        result = map_array_to_numbered_keys(["a"])
        self.assertIsInstance(list(result.keys())[0], str)

    def test_one_based_indexing(self):
        from scripts.dataforseo import map_array_to_numbered_keys

        result = map_array_to_numbered_keys(["first", "second"])
        self.assertIn("1", result)
        self.assertIn("2", result)
        self.assertNotIn("0", result)


if __name__ == "__main__":
    unittest.main()
