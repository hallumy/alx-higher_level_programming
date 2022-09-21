#!/usr/bin/python3
alpha = 122
while alpha >= 97:
    flag = 0
    if alpha % 2 != 0:
        alpha = alpha - 32
        flag = 1
    print("{:s}".format(chr(alpha)), end="")
    if flag == 1:
        alpha = alpha + 32
    alpha = alpha - 1
