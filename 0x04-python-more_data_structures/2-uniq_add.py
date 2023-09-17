#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum_int = 0
    unique = set(my_list)
    for i in unique:
        sum_int += i
    return sum_int
