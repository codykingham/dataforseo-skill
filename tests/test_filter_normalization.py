"""Test cases for filter normalization (remove_nested)."""

import os
import sys
import unittest

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


class TestFilterNormalization(unittest.TestCase):
    """Test remove_nested filter normalization."""

    def test_flat_filter_unchanged(self):
        """Flat filter array stays as-is: ["field","op","val"]."""
        from scripts.dataforseo import remove_nested

        filters = ["field", "op", "val"]
        result = remove_nested(filters)
        self.assertEqual(result, ["field", "op", "val"])

    def test_singly_nested_three_element_array_unchanged(self):
        """[["field","op","val"]] stays unchanged (inner has length 3, not 1)."""
        from scripts.dataforseo import remove_nested

        filters = [["field", "op", "val"]]
        result = remove_nested(filters)
        self.assertEqual(result, [["field", "op", "val"]])

    def test_compound_filter_with_and_unchanged(self):
        """Compound filter with "and" stays unchanged."""
        from scripts.dataforseo import remove_nested

        filters = [["field1", "=", "val1"], "and", ["field2", "=", "val2"]]
        result = remove_nested(filters)
        self.assertEqual(
            result, [["field1", "=", "val1"], "and", ["field2", "=", "val2"]]
        )

    def test_compound_filter_with_or_unchanged(self):
        """Compound filter with "or" stays unchanged."""
        from scripts.dataforseo import remove_nested

        filters = [["field1", "=", "val1"], "or", ["field2", "=", "val2"]]
        result = remove_nested(filters)
        self.assertEqual(
            result, [["field1", "=", "val1"], "or", ["field2", "=", "val2"]]
        )

    def test_null_filters(self):
        """None filters pass through."""
        from scripts.dataforseo import remove_nested

        result = remove_nested(None)
        self.assertIsNone(result)

    def test_empty_filters(self):
        """Empty filters pass through."""
        from scripts.dataforseo import remove_nested

        result = remove_nested([])
        self.assertEqual(result, [])

    def test_deeply_nested_single_arrays_unwrapped(self):
        """[[["field","op","val"]]] -> [["field","op","val"]] (TS unwraps one level)."""
        from scripts.dataforseo import remove_nested

        filters = [[["field", "op", "val"]]]
        result = remove_nested(filters)
        # TS behavior: outer[0] is [["field","op","val"]], length 1, inner is array
        # -> unwrap to ["field","op","val"]. Result is [["field","op","val"]].
        self.assertEqual(result, [["field", "op", "val"]])

    def test_mixed_nesting_partially_unwrapped(self):
        """Singly-nested elements get unwrapped while others stay."""
        from scripts.dataforseo import remove_nested

        filters = [
            [["field1", "=", "val1"]],
            "and",
            ["field2", "=", "val2"],
        ]
        result = remove_nested(filters)
        self.assertEqual(
            result,
            [["field1", "=", "val1"], "and", ["field2", "=", "val2"]],
        )


if __name__ == "__main__":
    unittest.main()
