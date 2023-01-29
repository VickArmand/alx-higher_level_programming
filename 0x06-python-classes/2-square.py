#!/usr/bin/python3

"""
Created on Jan 20 2023
@author : VickArmand

"""
class Square:

    """ A class that defines a square by its size """

    def __init__(self, size=0):

        """ Method to initialize the square object """

        if not isinstance(size, int):

            raise TypeError("size must be an integer")

        elif size < 0:

            raise ValueError("size must be >= 0")

        else:

            self.__size = int(size)
