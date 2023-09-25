#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    c = 0
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
            c = c + 1
    except:
        print()
        return c
    else:
        print()
        return c
