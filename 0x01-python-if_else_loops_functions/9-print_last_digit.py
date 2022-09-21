#!/usr/bin/python3
def print_last_digit(number):
    neg_num = 0
    if number < 0:
        number *= -1
    neg_num = 1
    num = number % 10
    if neg_num == 1:
        number *= -1
    print("{:d}".format(num), end="")
    return num
