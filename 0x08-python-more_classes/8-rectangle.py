#!/usr/bin/python3

"""Created by VickArmand """

class Rectangle:

    """This class defines a rectangle """

    number_of_instances = 0

    print_symbol = "#"

    def __init__(self, width = 0, height = 0):

        """ Method to initialize height and width"""

        self.__width = width

        self.__height = height

        Rectangle.number_of_instances += 1

    def __str__(self):

        """ Returns the informal representation"""

        rectangle = ""

        if self.__height == 0 or self.__width == 0:

            return rectangle

        else:

            for i in range(self.__height):

                rectangle += (Rectangle.print_symbol * self.__width) + "\n"

            return rectangle

    def __repr__(self):

        """ return a string representation of the rectangle """

        

        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):

        """ returns when an instance of Rectangle is deleted"""

        Rectangle.number_of_instances -= 1

        print("Bye Rectangle...") 

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

    def area(self):

        """ Returns the area of rectangle"""

        return self.__width * self.__height

    def perimeter(self):

        """ Returns the perimeter of rectangle"""

        if self.__height == 0 or self.__width == 0:

            return 0

        else:

            return (self.width + self.__height) * 2

    @staticmethod

    def bigger_or_equal(rect_1, rect_2):

        """ Returns if a rectangles area or perimeter is larger than another """

        if not isinstance(rect_1, Rectangle):

            raise TypeError("rect_1 must be an instance of Rectangle")

        elif not isinstance(rect_2, Rectangle):

            raise TypeError("rect_2 must be an instance of Rectangle")

        elif Rectangle.area(rect_1) == Rectangle.area(rect_2):

            return rect_1

        else:

            if Rectangle.area(rect_1) > Rectangle.area(rect_2):

                return rect_1

            else:

                return rect_2
