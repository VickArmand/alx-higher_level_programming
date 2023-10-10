#!/usr/bin/python3
"""
This module hosts class Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square that inherits from Rectangle"""
    def __init__(self, size):
        """
        Args
            size: length or width of square
        """
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """returns area of square"""
        return (self.__size ** 2)
