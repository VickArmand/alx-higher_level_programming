#!/usr/bin/python3
"""
This module hosts class Base
"""


class Base:
    """
    Class Atributes
        __nb_objects: number of objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Args
            id: integer
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
