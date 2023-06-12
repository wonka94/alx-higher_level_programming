#!/usr/bin/python3
"""Contains a single function"""


def add_attribute(self, name, value):
    """Add attribute if it's possible."""
    if hasattr(self, '__dict__'):
        setattr(self, name, value)
    else:
        raise TypeError("can't add new attribute")
