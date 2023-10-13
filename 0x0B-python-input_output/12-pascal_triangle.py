#!/usr/bin/python3
"""
This module hosts pascal_triangle function
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers
    representing the Pascal’s triangle of n
    Args
        n: integer
    """
    new_list = [[1]]
    if n <= 0:
        return []
    for i in range(1, n):
        length = len(new_list[i - 1])
        for j in range(length + 1):
            if j == 0:
                new_list.append([1])
            elif j == length:
                new_list[i].append(1)
            else:
                new_list[i].append(
                        new_list[i - 1][j - 1] + new_list[i - 1][j])
    return new_list
