#!/usr/bin/python3
"""This is the ``5-text_indentation`` module"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: ., ?, :

            Args:
                text(str): The text to print
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    text_len = len(text)
    chars = ".?:"
    index = 0
    lines = ""

    while True:
        while index < text_len and text[index] == " ":
            index += 1
        if index == text_len:
            break

        start = index
        while index < text_len and text[index] not in chars:
            index += 1

        if index == text_len:
            index -= 1
            while index > start and text[index] == " ":
                index -= 1

        index += 1

        line = text[start:index]
        if line:
            lines += line
            if line[index - start - 1] in chars:
                lines += "\n\n"

    print(lines, end="")
