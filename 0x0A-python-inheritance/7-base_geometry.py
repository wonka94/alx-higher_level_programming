#!/usr/bin/python3
"""Contains a `BaseGeometry` class"""


class BaseGeometry():
    """ BaseGeometry class """

    def area(self):
        """Calculates the area of the shape"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates that `value` is a positive integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
