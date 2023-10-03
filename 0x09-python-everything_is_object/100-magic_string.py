#!/usr/bin/python3
def magic_string(x=[0]):
    x[0] += 1
    return str("BestSchool, " * (x[0] - 1)) + "BestSchool"
