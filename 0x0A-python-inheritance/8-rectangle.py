#!/usr/bin/python3
""" Contains a class that inherits from `BaseGeometry """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Inherits from `BaseGeometry`"""
    def __init__(self, width, height):
        """Initialize rectangle value"""
        # Validate that width is a positive integer
        self.integer_validator("width", width)
        self.__width = width
        # Validate that height is a positive integer
        self.integer_validator("height", height)
        self.__height = height
