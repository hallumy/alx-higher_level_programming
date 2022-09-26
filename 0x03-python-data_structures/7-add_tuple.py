#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = [0, 0]
    b = [0, 0]
    for index, c in enumerate(tuple_a):
        if index < 2:
            a[index] = tuple_a[index]
    for index, c in enumerate(tuple_b):
        if index < 2:
            b[index] = tuple_b[index]
    sum_1 = a[0] + b[0]
    sum_2 = a[1] +b[1]
    return (sum_1, sum_2)
