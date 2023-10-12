#!/usr/bin/python3
"""
This module hosts to_json_string function
"""
import json


def to_json_string(my_obj):
    """
    returns the JSON representation of an object (string)
    Args
        my_obj: object to be represented
    """
    return json.dumps(my_obj)
