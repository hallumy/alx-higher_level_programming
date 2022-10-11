#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    number = 0
    try:
        for item in range(0, x):
            print("{}".format(my_list[item]), end="")
            number += 1
    except IndexError:
        pass
    print()
    return number
