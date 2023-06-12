#!/usr/bin/python3
"""Contains a single function"""


def inherits_from(obj, a_class):
    """
        Check if the object is an instance of a class
        that inherited (directly or indirectly) from
        the specified class
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
