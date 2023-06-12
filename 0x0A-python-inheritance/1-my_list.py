#!/usr/bin/python3
"""Contains `MyList` class"""


class MyList(list):
    """Class that extends the list base class"""

    def print_sorted(self):
        """Prints the list in ascending order"""
        print(sorted(self))
