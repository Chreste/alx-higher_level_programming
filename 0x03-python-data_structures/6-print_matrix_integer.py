#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
     for c in range(len(matrix)):
         for l in range(len(matrix[c])):
            if l != 0:
                print(" ", end='')
            print("{:d}".format(matrix[c][l]), end='')
            print()
