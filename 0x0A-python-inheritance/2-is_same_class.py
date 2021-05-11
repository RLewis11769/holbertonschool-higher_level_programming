#!/usr/bin/python3

"""
is_same_class - checks if given object is instance of given class
@obj: object to check
@a_class: class to check if obj is instance of
Return: True or False
"""


def is_same_class(obj, a_class):
    """ Returns boolean if obj is instance of a_class """
    return type(obj) == a_class
