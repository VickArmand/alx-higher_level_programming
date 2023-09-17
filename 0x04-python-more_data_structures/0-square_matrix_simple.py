#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = [list(map(lambda x: x**2, matrix[i])) for i in range(len(matrix))]
    return new
