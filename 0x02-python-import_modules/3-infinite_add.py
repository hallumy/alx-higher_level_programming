#!/usr/bin/python3
from sys import argv


def total(argv):
    length = len(argv) - 1
    if length == 0:
        print("{:d}".format(length))
        return
    else:
        index = 1
        totals = 0
        while index <= length:
            totals += int(argv[index])
            index += 1
        print("{:d}".format(totals))


if __name__ == "__main__":
    total(argv)
