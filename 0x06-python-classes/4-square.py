#!/usr/bin/python3
"""
Created by Vickarmand
Class square
"""


class Square:
    """
    Square that defines a square

    """
    def __init__(self, size=0):
        """
        __init__ method is run as soon as an object of a class is instantiated
        Args
            size (int / float): length of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """ size is a getter method for returning size of square """
        return self.__size

    @size.setter
    def size(self, value):
        """
        size is a setter method for replacing the existing size value
        Args
            value (int or float): value to replace size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        area returns the current square area
        """
        return self.__size ** 2
