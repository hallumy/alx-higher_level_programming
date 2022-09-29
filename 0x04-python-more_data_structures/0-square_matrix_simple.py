#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    temp = []
    for index in matrix:
        temp.append(list(map(lambda index: index ** 2, index)))
    return temp
