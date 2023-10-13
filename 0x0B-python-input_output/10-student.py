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
        """
        if type(attrs) == list and len(attrs) > 0 and all(
                type(elem) == str for elem in attrs):
            new_dict = dict()
            for i in attrs:
                if hasattr(self, i):
                    new_dict[i] = getattr(self, i)
            return new_dict
        else:
            return self.__dict__
