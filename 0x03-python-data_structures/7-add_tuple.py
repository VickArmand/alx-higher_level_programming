#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum_t = [0, 0]
    for i in range(2):
        element1 = 0
        element2 = 0
        try:
            element1 = tuple_a[i]
        except IndexError:
            element1 = 0
        try:
            element2 = tuple_b[i]
        except IndexError:
            element2 = 0
        sum_t[i] = element1 + element2
    return sum_t[0], sum_t[1]
