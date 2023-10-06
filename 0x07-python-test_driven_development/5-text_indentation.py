#!/usr/bin/python3
"""
This module has a function named text_indentation
"""


def text_indentation(text):
    """
    function that prints a text with 2 new lines
    after each of these characters:
    ., ? and :
    Args
        text - must be a string
    Raises
        TypeError - text must be a string - if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    flag = 0
    for char in text:
        if flag == 1 and char == ' ':
            continue
        if char == '.' or char == '?' or char == ':':
            flag = 1
            print(char)
            print()
        else:
            flag = 0
            print(char, end="")
