#!/usr/bin/python3
"""
This module hosts a function matrix_mul
"""


def matrix_mul(m_a, m_b):
    """
    multiplies 2 matrices
    Args
        m_a: must be an list of lists of integers or floats
        m_b: must be an list of lists of integers or floats
    Raises
        TypeError:
            m_a must be a list
            m_b must be a list
            m_a must be a list of lists
            m_b must be a list of lists
            m_a should contain only integers or floats
            m_b should contain only integers or floats
            each row of m_a must be of the same
            each row of m_b must be of the same size
        ValueError:
            m_a can't be empty
            m_b can't be empty
            m_a and m_b can't be multiplied
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if len(m_a) == 0:
        raise TypeError("m_a can't be empty")
    if len(m_b) == 0:
        raise TypeError("m_b can't be empty")
    columns_a = 0
    rows_b = len(m_b)
    for i in m_a:
        if type(i) != list:
            raise TypeError("m_a must be a list of lists")
        if len(i) == 0:
            raise ValueError("m_a can't be empty")
        if columns_a != len(i) and columns_a != 0:
            raise TypeError("each row of m_a must be of the same size")
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
        columns_a = len(i)
    columns_b = 0
    for x in m_b:
        if type(x) != list:
            raise TypeError("m_b must be a list of lists")
        if len(x) == 0:
            raise ValueError("m_b can't be empty")
        if columns_b != len(x) and columns_b != 0:
            raise TypeError("each row of m_b must be of the same size")
        for y in x:
            if not isinstance(y, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
        columns_b = len(x)
    if rows_b != columns_a:
        raise ValueError("m_a and m_b can't be multiplied")
    matrix = []
    for rows in m_a:
        i = 0
        row_list = []
        while i < len(m_b[0]):
            k = 0
            sum_prod = 0
            for col in rows:
                sum_prod += col * m_b[k][i]
                k += 1
            row_list.append(sum_prod)
            i += 1
        matrix.append(row_list)
    return matrix
