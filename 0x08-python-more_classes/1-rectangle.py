#!/usr/bin/python3

"""Created by VickArmand """

class Rectangle:

    """This class defines a rectangle """

   
    def __init__(self, width = 0, height = 0):

        """ Method to initialize height and width"""

        self.__width = width

        self.__height = height

    def __str__(self):

        """ Returns the informal representation"""

        if self.__height == 0 or self.__width == 0:

            return ""

        else:

            for i in range(0,self.__width):

                for j in range(0,self.__height):

                    print("#")

                print()

    @property

    def width(self):

        """ A getter for the width property"""

        return self.__width

    @width.setter

    def width(self, value):

        """ A setter for the width property"""

        if not isinstance(value, int):

            raise TypeError("width must be an integer")

        elif(value < 0):

            raise ValueError("width must be >= 0")

        else:

            self.__width = value

    @property

    def height(self):

        """ A getter for the height property"""

        return self.__height

    @height.setter

    def height(self, value):

        """ A setter for the height property"""

        if not isinstance(value, int):

            raise TypeError("height must be an integer")

        elif(value < 0):

            raise ValueError("height must be >= 0")

        else:

            self.__height = value 
