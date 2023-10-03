#!/usr/bin/python3
"""
Created by vickarmand
class Rectangle
"""


class Rectangle:
    """
    class Rectangle defines a rectangle
    number_of_instances: public class attribute
    which stores the number of existing objects
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        __init__ method is run as soon as an object of a class is instantiated
        Args
            width: width of rectangle
            height: height of rectangle
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ width is a getter method for retrieving the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        width is a setter method for assigning a new value for the width
        Args
            value: new integer value to replace the existing width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height is a getter method for retrieving height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        height is a setter method for assigning a new height
        Args
            value: new integer value to replace existing height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """returns the rectangle's blueprint with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            string = "\n".join("#" * self.__width for j in range(
                self.__height))
            return string

    def __repr__(self):
        """"
        return a string representation of the rectangle
        to be able to recreate a new instance by using eval()
        """
        string = "Rectangle("
        string += str(self.__width) + ", " + str(self.__height) + ")"
        return string

    def __del__(self):
        """Print the message Bye rectangle... (... being 3 dots not ellipsis)
        when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
        del (self)
