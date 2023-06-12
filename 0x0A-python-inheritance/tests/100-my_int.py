#!/usr/bin/python3
"""Contains a class `MyInt` that inherits from `int`"""


class MyInt(int):
    """Inherits from int base class"""
    def __eq__(self, num):
        """Invert the == operator"""
        return super().__ne__(num)

    def __ne__(self, num):
        """Invert the != operator"""
        return super().__eq__(num)

