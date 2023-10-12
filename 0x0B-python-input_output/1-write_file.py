#!/usr/bin/python3
"""
This module hosts write_file function
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8)
    and returns the number of characters written
    Args
        filename: name of file
        text: text to be appended
    """
    with open(filename, "w", encoding="utf-8") as f:
        bytes_written = f.write(text)
    return bytes_written
