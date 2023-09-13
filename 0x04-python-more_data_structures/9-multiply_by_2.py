#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = {}
    for x in a_dictionary:
        new_dic[x] = a_dictionary[x] * 2
    return new_dic
