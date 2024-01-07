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
    end = len(list_of_integers) - 1
    start = 0
    ls = list_of_integers
    if ls[start] > ls[start + 1]:
        return ls[start]
    if ls[end] > ls[end - 1]:
        return ls[end]
    mid = (end + start) // 2
    if ls[mid] > ls[mid - 1] and ls[mid] > ls[mid + 1]:
        return ls[mid]
    if ls[mid] < ls[mid - 1]:
        return find_peak(ls[:mid - 1])
    elif ls[mid] < ls[mid + 1]:
        return find_peak(ls[mid:])
    else:
        return ls[start]
