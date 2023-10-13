#!/usr/bin/python3
"""
This module hosts class Student
"""


class Student:
    """defines a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance
        Args
            attrs: is a list of strings,
            only attributes name contain in this list must be retrieved.
        """
        if type(attrs) == list and len(attrs) > 0 and all(type(elem) == str for elem in attrs):
            new_dict = dict()
            for i in attrs:
                if hasattr(self, i):
                    new_dict[i] = getattr(self, i)
            return new_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        replaces all attributes of the Student instance
        Args
            json: a dictionary containing attributes and
            the values to be replaced
        """
        for i in json.keys():
            if hasattr(self, i):
                setattr(self, i, json[i])
