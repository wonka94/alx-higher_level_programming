#!/usr/bin/python3
""" `append_write` module"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file
       and returns the number of characters added"""

    num = 0

    with open(filename, "a", encoding="utf-8") as f:
        num = f.write(text)

    return num
