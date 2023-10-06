#!/usr/bin/python3
"""
The module has a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Args
        matrix: must be a list of lists of integers or floats
        div: must be a number (integer or float)
    Raises
        TypeError exception with the message
            matrix must be a matrix (list of lists) of integers/floats
            Each row of the matrix must have the same size
            if each row of matrix is not of same size
            div must be a number if div is not a number
        ZeroDivisionError exception with the message
            division by zero if div is equal to 0
    Returns
        new matrix where by all elements of the matrix should be
        divided by div, rounded to 2 decimal places
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    length = 0
    for row in range(len(matrix)):
        if not isinstance(matrix[row], list):
            raise TypeError(msg)
        if len(matrix[row]) != length and length != 0:
            raise TypeError("Each row of the matrix must have the same size")
        for i in range(len(matrix[row])):
            if not isinstance(
                    matrix[row][i], (int, float)):
                raise TypeError(msg)
        length = len(matrix[row])
    res = list(list(map(lambda x: round(x / div, 2), i)) for i in matrix)
    return res
