#!/usr/bin/python3
def weight_average(my_list=[]):
    score = 0
    weight = 0
    if len(my_list) == 0:
        return 0
    for i in my_list:
        prod = 1
        length = len(i)
        weight += i[length - 1]
        for j in i:
            prod *= j
        score += prod
    return score / weight
