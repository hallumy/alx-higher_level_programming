#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    string = "arguments"
    punc = "."
    length = len(argv) - 1
    if length == 1:
        string = "argument"
    if length > 0:
        punc = ":"
    print("{:d} {:s}{}".format(length, string, punc))
    for index, arg in enumerate(argv):
        if(index > 0):
            print("{:d}: {:s}".format(index, arg))
