#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    m = len(my_list)
    if m == 0:
        return
    for x in range(m - 1, -1, -1):
        print(str.format("{}", my_list[x]))
