#!/usr/bin/python3
"""Defines a test case for the base.py module in the models directory."""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json


class TestBaseClass(unittest.TestCase):
    """A class that inherits from unittest.
       TestCase and tests the Base class."""

    def test_id_none(self):
        """Tests initializing an instance of the
           Base class with no id argument.

        Asserts that the id attribute is equal to 1,
        which is the default value.
        """
        b = Base()
        self.assertEqual(1, b.id)

    def test_id(self):
        """Tests initializing an instance of the Base
           class with a positive id argument.

        Asserts that the id attribute is equal to the given argument.
        """
        b = Base(2)
        self.assertEqual(2, b.id)

    def test_id_zero(self):
        """Tests initializing an instance of the Base
           class with a zero id argument.

        Asserts that the id attribute is equal to zero.
        """
        b = Base(0)
        self.assertEqual(0, b.id)

    def test_id_negative(self):
        """Tests initializing an instance of the Base
           class with a negative id argument.

        Asserts that the id attribute is equal to the given argument.
        """
        b = Base(-2)
        self.assertEqual(-2, b.id)

    def test_id_string(self):
        """Tests initializing an instance of the Base
           class with a string id argument.

        Asserts that the id attribute is equal to the given string.
        """
        b = Base("Base")
        self.assertEqual("Base", b.id)

    def test_id_list(self):
        """Tests initializing an instance of the Base
           class with a list id argument.

        Asserts that the id attribute is equal to the given list.
        """
        b = Base([1, 2, 3])
        self.assertEqual([1, 2, 3], b.id)

    def test_id_tuple(self):
        """Tests initializing an instance of the Base
           class with a tuple id argument.

        Asserts that the id attribute is equal to the given tuple.
        """
        b = Base((1, 3))
        self.assertEqual((1, 3), b.id)

    def test_id_dict(self):
        """Tests initializing an instance of the Base
           class with a dictionary id argument.

        Asserts that the id attribute is equal to the given dictionary.
        """
        b = Base({'id': 5})
        self.assertEqual({'id': 5}, b.id)

    def test_to_json_type(self):
        """Tests converting a dictionary representation
           of a Square instance to JSON string.

        Asserts that the type of the JSON string is str.
        """
        sq = Square(5)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(type(json_string), str)

    def test_to_json_value(self):
        """Tests converting a dictionary representation
           of a Square instance to JSON string.

         Asserts that the value of the JSON string matches
         the expected output. Uses json.loads() to compare two dictionaries.
         """
        sq = Square(2, 3, 3, 1)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(json.loads(json_string), [{"id": 1, "x": 3,
                                                    "y": 3, "size": 2}])

    def test_to_json_None(self):
        """Tests converting None to JSON string.

        Asserts that the JSON string is equal to "[]".
        """
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_empty(self):
        """Tests converting an empty list to JSON string.

        Asserts that the JSON string is equal to "[]".
        """
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_from_json_string(self):
        """Tests converting a JSON string to a list of dictionaries.

        Asserts that the list of dictionaries matches the expected output.
        Uses json.loads() to compare two dictionaries.
        """
        sq = Square(1, 3, 3, 4)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        json_list = Base.from_json_string(json_string)
        self.assertEqual(json_list, [{'size': 1, 'x': 3, 'y': 3, 'id': 4}])

    def test_from_json_none(self):
        """Tests converting None to a list of dictionaries.

        Asserts that the list of dictionaries is empty.
        """
        json_list = Base.from_json_string(None)
        self.assertEqual(json_list, [])

    def test_from_json_empty(self):
        """Tests converting an empty JSON string to a list of dictionaries.

        Asserts that the list of dictionaries is empty.
        """
        json_list = Base.from_json_string([])
        self.assertEqual(json_list, [])
