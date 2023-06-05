#!/usr/bin/python3

"""Define class rectangle with width and height attributes"""


class Rectangle():
    """Represent a rectangle
    Args:
        width (int): width
        height (int): height

    Functions:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
        area(self)
        perimeter(self)
        __str__(self)
    """
    def __init__(self, width=0, height=0):
        """ Initialize rectangles """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter returns width """
        return self.__width

    @property
    def height(self):
        """ Getter returns height """
        return self.__height

    @width.setter
    def width(self, value):
        """ Set width if int > 0 """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Returns height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets height if int > 0 """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def perimeter(self):
        """
           Return perimeter of the rectangle
           Return 0 if width or height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        perimeter = (self.__width * 2) + (self.height * 2)
        return perimeter

    def area(self):
        """
           Return area of the rectangle
           Return 0 if width or height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        area = self.__width * self.__height
        return area

    def __str__(self):
        """
           Prints rectangle with # symbol
           Print an empty string if width of height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rec = "\n".join(["#" * self.__width for rows in range(self.__height)])
        return rec
