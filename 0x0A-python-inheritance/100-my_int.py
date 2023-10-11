#!/usr/bin/python3
"""
This module hosts MyInt class
"""


class MyInt(int):
    """MyInt that inherits from int"""
    def __eq__(self, other):
        """what was != is now =="""
        return int(self) != other

    def __ne__(self, other):
        """what was == is now !="""
        return int(self) == other
