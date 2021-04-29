#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for down in matrix:
        for across in down:
            print("{:d}".format(across), end=" ")
        print()
