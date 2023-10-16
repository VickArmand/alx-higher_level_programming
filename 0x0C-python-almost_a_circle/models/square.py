#!/usr/bin/python3
"""
This module hosts class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        Args
            size: integer value > 0
            x: integer value >= 0
            y: integer value >= 0
            id: integer value
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter - returns the width of Square"""
        return self.width

    @size.setter
    def size(self, value):
        """
        size setter - changes the width of Square
        Args
            value: integer > 0
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def area(self):
        """returns the area value of the Square instance"""
        return self.width * self.height

    def display(self):
        """prints in stdout the Square instance with the character #"""
        for y in range(self.y):
            print()
        for row in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for col in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """overriding the __str__ method to return object description"""
        string = "[Square] (" + str(self.id) + ") " + str(self.x)
        string += "/" + str(self.y) + " - "
        string += str(self.width)
        return string

    def update(self, *args, **kwargs):
        """
        Update the attributes of a Square instance
        Args
            args: a composition of stacked arguments
            kwargs: a composition of key value arguments
        """
        try:
            if len(args) > 0 and len(kwargs) == 0:
                self.id = args[0]
                self.width = args[1]
                self.height = args[1]
                self.x = args[2]
                self.y = args[3]
            else:
                for key in kwargs:
                    if key == "id":
                        self.id = kwargs[key]
                    if key == "size":
                        self.width = kwargs[key]
                        self.height = kwargs[key]
                    if key == "x":
                        self.x = kwargs[key]
                    if key == "y":
                        self.y = kwargs[key]
        except IndexError:
            pass

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        new_dict = {'id': self.id, 'x': self.x, 'size': self.height,
                    'y': self.y}
        return new_dict
