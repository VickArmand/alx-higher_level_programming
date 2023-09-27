#!/usr/bin/python3
"""
Created by Vickarmand
Class square
"""


class Square:
    """
    Square that defines a square

    """
    def __init__(self, size=0, position=(0, 0)):
        """
        __init__ method is run as soon as an object of a class is instantiated
        Args
            size (int / float): length of square
            position (tuple): a tuple of x and y coordinates
        """
        self.__position = position
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

    @property
    def position(self):
        """ position is a getter for retrieving the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """
        position is a settef for modifying the existing position
        Args
            value (tuple): replacement for position field
        """
        if (isinstance(value, tuple) and len(value) == 2) and (
                value[0] >= 0 and value[1] >= 0):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """
        area returns the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """ prints in stdout the square with the character # """
        if (self.__size == 0):
            print()
        else:
            for k in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
