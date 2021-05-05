#!/usr/bin/python3

"""
add_integer - adds 2 integers
@a: first integer to add
@b: second integer to add (default 98)
Return: sum of addition of a and b
"""


def add_integer(a, b=98):
    """ Adds 2 integers """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    return a + b
