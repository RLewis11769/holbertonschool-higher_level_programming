#!/usr/bin/python3

"""
prints a square of #
@size: length of each side of square
"""


def print_square(size):
    """ prints square of size with # """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for across in range(size):
        for down in range(size):
            print("#", end="")
        print()
