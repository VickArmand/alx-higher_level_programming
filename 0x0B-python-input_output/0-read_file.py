#!/usr/bin/python3
"""
This module hosts read_file function
"""


def read_file(filename=""):
    """
    reads a text file (UTF8) and prints it to stdout
    Args
        filename: name of file
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
