#!/usr/bin/python3
"""
This module hosts the class Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """
        Args
            width: width
            height: height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """area of rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """
        returns the following rectangle description:
        [Rectangle] <width>/<height>
        """
        string = "[Rectangle] " + str(self.__width)
        string += "/" + str(self.__height)
        return string
