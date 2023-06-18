#!/usr/bin/python3
"""Defines a class that inherits from Rectangle."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """A class that inherits from Rectangle and represents a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the attributes of the square.

        Args:
            size (int): The length of the sides of the square.
            x (int): The horizontal position of the square.
            y (int): The vertical position of the square.
            id (int): The unique identifier of the square.
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """The size property getter.

        Returns:
            int: The length of the sides of the square.
        """

        return self.width

    @size.setter
    def size(self, value):
        """The size property setter.

        Args:
            value (int): The new length of the sides of the square.
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the attributes of the square."""

        if args and len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """
        Returns:
            dict: A dictionary with keys and values for each attribute.
        """
        # Use a dictionary literal to create and return the dictionary
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Returns a string representation of the square.

        Returns:
            str: A formatted string with information about the square.
        """
        _id = self.id
        x = self.x
        y = self.y
        size = self.size
        return "[Square] ({}) {}/{} - {}".format(_id, x, y, size)
