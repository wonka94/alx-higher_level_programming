#!/usr/bin/python3
"""Defines a test case for the rectangle.py module in the models directory."""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """A class that tests the Rectangle class."""

    def test_init(self):
        """Tests initializing an instance of the Rectangle
           class with valid arguments.

        Asserts that the attributes are equal to the given arguments.
        """
        r = Rectangle(5, 6, 2, 3, 4)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 4)

    def test_init_invalid_width(self):
        """Tests initializing an instance of the
           Rectangle class with an invalid width argument.

        Asserts that a TypeError or ValueError is raised
        depending on the type and value of width.
        """
        with self.assertRaises(TypeError):
            r = Rectangle("a", 1)
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 1)

    def test_init_invalid_height(self):
        """Tests initializing an instance of the
           Rectangle class with an invalid height argument.

        Asserts that a TypeError or ValueError is raised
        depending on the type and value of height.
        """
        with self.assertRaises(TypeError):
            r = Rectangle(1, "b")
        with self.assertRaises(ValueError):
            r = Rectangle(1, -2)

    def test_init_invalid_x(self):
        """Tests initializing an instance of the
           Rectangle class with an invalid x argument.

        Asserts that a TypeError or ValueError is raised
        depending on the type and value of x.
        """
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, "c")
        with self.assertRaises(ValueError):
            r = Rectangle(1, 1, -3)

    def test_init_invalid_y(self):
        """Tests initializing an instance of the
           Rectangle class with an invalid y argument.

        Asserts that a TypeError or ValueError is raised
        depending on the type and value of y.
        """
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, 0, "d")
        with self.assertRaises(ValueError):
            r = Rectangle(1, 1, 0, -4)

    def test_area(self):
        """Tests calculating the area of an
           instance of the Rectangle class.

        Asserts that the area is equal to the
        product of width and height.
        """
        r = Rectangle(5, 6)
        self.assertEqual(r.area(), 30)

    def test_update_args(self):
        """Tests updating the attributes of an instance
           of the Rectangle class using positional arguments.

        Asserts that the attributes are equal to the given arguments.
        """
        r = Rectangle(1, 1)
        r.update(10)
        self.assertEqual(r.id, 10)
        r.update(10, 2)
        self.assertEqual(r.width, 2)
        r.update(10, 2, 3)

    def test_to_dictionary(self):
        """Tests converting an instance of the Rectangle
           class to a dictionary.

        Asserts that the dictionary representation
        matches the expected output.
        """
        r = Rectangle(5, 6, 2, 3, 4)
        d = r.to_dictionary()
        self.assertEqual(d, {"x": 2, "y": 3, "id": 4, "height": 6, "width": 5})
