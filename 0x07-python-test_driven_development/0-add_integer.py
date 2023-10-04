#!/usr/bin/python3
"""
0-add_integer - contains the add function
"""


def add_integer(a, b=98):
    """ add - function that adds 2 integers."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
