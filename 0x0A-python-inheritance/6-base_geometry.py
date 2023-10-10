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
