#!/usr/bin/python3
"""
This module has the lookup function
"""


def lookup(obj):
    """
    lookup returns the list of available attributes
    and methods of an object
    Args
        obj: object
    Return: a list object
    """
    return dir(obj)
