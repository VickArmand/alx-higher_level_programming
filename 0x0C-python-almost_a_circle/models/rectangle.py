#!/usr/bin/python3
"""
This module hosts class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Args
            width: rectangle width
            height: rectangle height
            x:x
            y:y
            id:id
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if type(x) != int:
            raise TypeError("x must be an integer")
        if type(y) != int:
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """getter for the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter for the width attribute
        Args
            value: integer
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter for the height attribute
        Args
            value: integer
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for the x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """
        setter for the x attribute
        Args
            value: integer
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for the y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """
        setter for the y attribute
        Args
            value: integer
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for y in range(self.__y):
            print()
        for row in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for col in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """overriding the __str__ method to return object description"""
        string = "[Rectangle] (" + str(self.id) + ") " + str(self.__x)
        string += "/" + str(self.__y) + " - "
        string += str(self.__width) + "/" + str(self.__height)
        return string

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        Args
            args: a composition of stacked arguments
            kwargs: a composition of key value arguments
        """
        try:
            if len(args) > 0 and len(kwargs) == 0:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            else:
                for key in kwargs:
                    if key == "width":
                        self.__width = kwargs[key]
                    if key == "height":
                        self.__height = kwargs[key]
                    if key == "id":
                        self.id = kwargs[key]
                    if key == "x":
                        self.__x = kwargs[key]
                    if key == "y":
                        self.__y = kwargs[key]
        except IndexError:
            pass

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        new_dict = {'x': self.x, 'y': self.y, 'id': self.id,
                    'height': self.height, 'width': self.width}
        return new_dict
