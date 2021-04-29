#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for down in matrix:
        for across in down:
            if across == down[0]:
                print("{:d}".format(across), end="")
            else:
                print(" {:d}".format(across), end="")
        print()
