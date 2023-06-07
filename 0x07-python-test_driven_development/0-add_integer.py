#!/usr/bin/python3
"""
This is the "0-add_integer" module.
The 0-add_integer module supplies one function, add_integer(). For example,
>>> add_integer(1, 2)
"""


def add_integer(a, b=98):
    """
        Adds two integers
        Args:
            a (int|float): An integer or float
            b (int|float): An integer or float
        Returns: The sum of a and b
    """

    if type(a) is float:
        a = int(a)

    if type(b) is float:
        b = int(b)

    if not isinstance(a, int):
        raise TypeError("a must be an integer")

    if not isinstance(b, int):
        raise TypeError("b must be an integer")

    sum = a + b

    return sum
