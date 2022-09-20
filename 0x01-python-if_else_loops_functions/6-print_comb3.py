#!/usr/bin/python3
for num in range(0, 9):
    for digit in range(num + 1, 10):
        if num == 8 and digit == 9:
            print("{:d}{:d}".format(num, digit))
        else:
            print("{:d}{:d}".format(num, digit), end=", ")
