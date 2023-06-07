#!/usr/bin/python3
"""
This is the ``2-matrix_divided`` module.
The 2-matrix_divided module provides one function. matrix_divided().
"""


def matrix_divided(matrix, div):
    """
        A function that divides all elements of a matrix.

            Args:
                matrix (list): A list of lists
                div (int|float): A integer of a float
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    err = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(err)

    row_size = 0
    if matrix and isinstance(matrix[0], list):
        row_size = len(matrix[0])

    new_matrix = []
    for row in matrix:
        new_row = []
        if not isinstance(row, list):
            raise TypeError(err)

        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

        for value in row:
            if not isinstance(value, (int, float)):
                raise TypeError(err)
            new_row.append(round(value / div, 2))

        new_matrix.append(new_row)

    return new_matrix
