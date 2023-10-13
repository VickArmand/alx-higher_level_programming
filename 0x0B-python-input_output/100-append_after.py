#!/usr/bin/python3
"""
This module hosts append_after function
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file,
    after each line containing a specific string
    Args
        filename: name of file
        search_string: search word
        new_string: text to be appended
    """
    data = []
    with open(filename, "r") as f:
        line = f.readline()
        while line != "":
            if search_string in line:
                data.append(line)
                data.append(new_string)
            else:
                data.append(line)
            line = f.readline()
    with open(filename, "w") as f:
        f.writelines(data)
