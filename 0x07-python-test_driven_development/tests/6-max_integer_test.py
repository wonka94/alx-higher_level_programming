#!/usr/bin/python3
"""Unittests for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class Max_Integer(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def max_at_begginning(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def floats(self):
        """Test a list of floats."""
        floats = [8.33, 2.54, 8.4, -4.8]
        self.assertEqual(max_integer(floats), 8.33)

    def ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [6, 2.43, 4.8, 3.35]
        self.assertEqual(max_integer(ints_and_floats), 6)

    def string(self):
        """Test a string."""
        string = "Hello World"
        self.assertEqual(max_integer(string), 'o')

    def list_of_strings(self):
        """Test a list of strings."""
        strings = ["Welcome", "to", "unit", "testing"]
        self.assertEqual(max_integer(strings), "unit")

    def empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
