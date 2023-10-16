#!/usr/bin/python3
"""
This module hosts class Base
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        Args
            list_dictionaries: list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """"
        writes the JSON string representation of list_objs to a file
        Args
            cls: class
            list_objs: is a list of instances who inherits of Base
        """
        filename = cls.__name__+".json"
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write(Base.to_json_string([]))
            else:
                f.write(Base.to_json_string(
                    [obj.to_dictionary() for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        Args
            json_string: a string representing a list of dictionaries
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        Args
            cls: class
            dictionary: keyword argument
        """
        if dictionary is not None and dictionary != {}:
            obj = cls(4, 4, 2, 2)
            obj.update(**dictionary)
            return obj

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__+".json"
        try:
            with open(filename, "r") as f:
                data = f.read()
            obj = Base.from_json_string(data)
            return [cls.create(**o) for o in obj]
        except FileNotFoundError:
            return []