#!/usr/bin/python3
""" `write_file` module"""


def write_file(filename="", text=""):
    """Write a string to a text file and returns
       the number of characters written"""

    num = 0

    with open(filename, "w", encoding="utf-8") as f:
        num = f.write(text)

    return num
