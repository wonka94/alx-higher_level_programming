#!/usr/bin/python3
"""Contains a single function"""


def is_same_class(obj, a_class):
    """
        Check if an object is exactly an instance of the specified class
    """

    return (type(obj) == a_class)
