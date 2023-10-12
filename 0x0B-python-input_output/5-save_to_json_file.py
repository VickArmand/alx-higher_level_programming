#!/usr/bin/python3
"""
This module hosts save_to_json_file function
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation
    Args
        my_obj: Python data structure
        filename: name of file
    """
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
