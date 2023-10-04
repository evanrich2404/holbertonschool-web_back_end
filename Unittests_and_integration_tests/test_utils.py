#!/usr/bin/env python3
"""Unit tests for utils.py"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessnestedMap(unittest.TestCase):
    """Test access_nested_map function"""

    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map function"""
        @parameterized.expand([
            nested_map={"a": 1}, path=("a",)
            nested_map={"a": {"b": 2}}, path=("a",)
            nested_map={"a": {"b": 2}}, path=("a", "b")
        ])
        self.assertEqual(access_nested_map(nested_map, path), expected)
