#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
 [print("{}: {}".format(ch, a_dictionary[ch])) for ch in sorted(a_dictionary)]
