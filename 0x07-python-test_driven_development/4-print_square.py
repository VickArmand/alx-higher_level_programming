#!/usr/bin/python3
"""
This module has a function print_square
"""


def print_square(size):
    """
    prints a square with the character #.
    Args:
        size: size length of the square and must be int
    Raise:
        TypeError:
            size must be an integer - if size is not an int
        ValueError:
            size must be >= 0 - if size is less than 0
    """
    if not isinstance(size, (int)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
