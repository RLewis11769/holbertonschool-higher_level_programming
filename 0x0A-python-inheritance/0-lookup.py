#!/usr/bin/python3

"""
lookup - finds attributes and methods of given object
@obj: object to find attributes and methods of
Return: list containing attributes and methods
"""


def lookup(obj):
    """ finds list of attributes and methods of obj """
    return dir(obj)
