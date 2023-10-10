#!/usr/bin/python3
"""
This module holds a class MyList
"""


class MyList(list):
    """MyList that inherits from list"""
    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        new = self[:]
        new.sort()
        print(new)
