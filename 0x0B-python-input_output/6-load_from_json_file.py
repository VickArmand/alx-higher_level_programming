#!/usr/bin/python3
"""
This module hosts load_from_json_file function
"""
import json


def load_from_json_file(filename):
    """
    creates an Object from a JSON file
    Args
        filename: name of file
    """
    with open(filename, "r") as f:
        json_obj = f.read()
    return (json.loads(json_obj))
