#!/usr/bin/python3
"""
This module hosts the magic_calculation function
that implements the following bytecode
3       0 LOAD_CONST    1 (98)
        3 LOAD_FAST     0 (a)
        6 LOAD_FAST     1 (b)
        9 BINARY_POWER
        10 BINARY_ADD
        11 RETURN VALUE
"""


def magic_calculation(a, b):
    """"""
    return 98 + a ** b
