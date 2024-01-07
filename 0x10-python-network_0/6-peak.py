#!/usr/bin/python3
"""
This module hosts the find_peak function
"""


def find_peak(list_of_integers):
    """
    function that finds a peak in a list of unsorted integers
    """
    if len(list_of_integers) == 0:
        return None
    elif type(list_of_integers) is not list:
        return list_of_integers
    else:
        length = len(list_of_integers) - 1
        peak = list_of_integers[0]
        for i in range(length):
            if list_of_integers[i] > peak:
                peak = list_of_integers[i]
        return peak
