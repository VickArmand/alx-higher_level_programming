#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum_t = [0, 0]
    for i in range(2):
        element1 = 0
        element2 = 0
        if tuple_a[i] is None:
            element1 = 0
        elif tuple_b[i] is None:
            element2 = 0
        else:
            element1 = tuple_a[i]
            element2 = tuple_b[i]
        sum_t[i] = element1 + element2
    return sum_t[0], sum_t[1]


