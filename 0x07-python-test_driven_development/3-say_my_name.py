#!/usr/bin/python3
"""
This is the ``say_my_name`` module.
The say_my_name module provides one function, say_my_name().
"""


def say_my_name(first_name, last_name=""):
    """
        this functions prints a string:
        e.g: My name is 'fist name' 'last name'

        Args:
            first_name(str): The first name
            last_name(str): The last name (Optional)
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
