#!/usr/bin/python3
"""
This module holds say_my_name function
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name: function that prints a persons full name
    Raises
        TypeError:
            if first_name must be a string - raised
            if first_name is not a string
            last_name must be a string - raised if last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
