#!/usr/bin/python3
"""Defines a test case for the square.py module in the models directory."""
import unittest
import io
import sys
from models.base import Base
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """A class that tests the Square class."""

    def test_init(self):
        """Tests initializing an instance of the Square
           class with valid arguments.

        Asserts that the attributes are equal to the given arguments.
        """
        sq = Square(5, 2, 3, 4)
        self.assertEqual(sq.size, 5)
        self.assertEqual(sq.x, 2)
        self.assertEqual(sq.y, 3)
        self.assertEqual(sq.id, 4)

    def test_init_invalid_size(self):
        """Tests initializing an instance of the Square class with
           an invalid size argument.

        Asserts that a TypeError or ValueError is raised depending
        on the type and value of size.
        """
        with self.assertRaises(TypeError):
            sq = Square("a")
        with self.assertRaises(ValueError):
            sq = Square(-1)

    def test_init_invalid_x(self):
        """Tests initializing an instance of the Square class with
           an invalid x argument.

        Asserts that a TypeError or ValueError is raised depending
        on the type and value of x.
        """
        with self.assertRaises(TypeError):
            sq = Square(1, "b")
        with self.assertRaises(ValueError):
            sq = Square(1, -2)

    def test_init_invalid_y(self):
        """Tests initializing an instance of the Square class with
           an invalid y argument.

        Asserts that a TypeError or ValueError is raised depending
        on the type and value of y.
        """
        with self.assertRaises(TypeError):
            sq = Square(1, 0, "c")
        with self.assertRaises(ValueError):
            sq = Square(1, 0, -3)

    def test_str(self):
        """Tests converting an instance of the Square class to a string.

        Asserts that the string representation matches the expected output.
        """
        sq = Square(5, 2, 3, 4)
        self.assertEqual(str(sq), "[Square] (4) 2/3 - 5")

    def test_update_args(self):
        """Tests updating the attributes of an instance of the
           Square class using positional arguments.

        Asserts that the attributes are equal to the given arguments.
        """
        sq = Square(1)
        sq.update(10)
        self.assertEqual(sq.id, 10)
        sq.update(10, 2)
        self.assertEqual(sq.size, 2)
        sq.update(10, 2, 3)
