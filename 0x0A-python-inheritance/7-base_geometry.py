#!/usr/bin/python3
"""
This module hosts class BassGeometry
"""


class BaseGeometry:
    """BaseGeometry"""
    def area(self):
        """
        that raises an Exception with the message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value
        Args
            name: name
            value: value
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
