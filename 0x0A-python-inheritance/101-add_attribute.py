#!/usr/bin/python3
"""
This module hosts add_attribute function
"""


def add_attribute(obj, attr, value):
    """
    adds a new attribute to an object if it’s possible
    Args
        attr: attribute
        value: attribute value
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
