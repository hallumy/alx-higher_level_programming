#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    temp = a_dictionary.copy()
    for index in temp.keys():
        temp[index] *= 2
    return temp
