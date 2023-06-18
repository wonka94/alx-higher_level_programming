#!/usr/bin/python3
"""Defines a class that inherits from Base and represents a rectangle."""

from models.base import Base


class Rectangle(Base):
    """A class that inherits from Base and represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the attributes of the rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The horizontal position of the rectangle.
            y (int): The vertical position of the rectangle.
            id (int): The unique identifier of the rectangle.
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """The width property getter.

        Returns:
            int: The width of the rectangle.
        """

        return self.__width

    @width.setter
    def width(self, value):
        """The width property setter.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to zero.
        """

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """The height property getter.

        Returns:
            int: The height of the rectangle.
        """

        return self.__height

    @height.setter
    def height(self, value):
        """The height property setter.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to zero.
        """

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """The x property getter.

        Returns:
            int: The horizontal position of the rectangle.
        """

        return self.__x

    @x.setter
    def x(self, value):
        """The x property setter.

        Args:
            value (int): The new horizontal position of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """

        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """The y property getter.

        Returns:
            int: The vertical position of the rectangle.
        """

        return self.__y

    @y.setter
    def y(self, value):
        """The y property setter.

        Args:
            value (int): The new vertical position of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """

        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle.

        Returns:
            int: The product of width and height.
        """

        return self.__width * self.__height

    def display(self):
        """Prints the rectangle to stdout using the character "#"."""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """Returns a string representation of the rectangle.

        Returns:
            str: A formatted string with information about the rectangle.
        """
        ID = self.id
        x = self.__x
        y = self.__y
        width = self.__width
        height = self.__height
        return "[Rectangle] ({}) {}/{} - {}/{}".format(ID, x, y, width, height)

    def update(self, *args, **kwargs):
        """Updates the attributes of the rectangle."""

        if args and len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """
            Returns the dictionary representation of the rectangle
        """
        return {"x": self.__x,
                "y": self.__y,
                "id": self.id,
                "height": self.__height,
                "width": self.__width
                }
