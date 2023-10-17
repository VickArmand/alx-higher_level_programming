#!/usr/bin/python3
"""
This module hosts lazy_matrix_mul function
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    multiplies 2 matrices by using the module NumPy
    Args
        m_a: matrix a
        m_b: matrix b
    """
    return np.multiply(m_a, m_b)
