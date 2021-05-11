#!/usr/bin/python3

"""
is_kind_of_class - checks if given object is instance or inherits from class
@obj: object to check
@a_class: class to check if obj inherits from given class
Return: True or False
"""


def is_kind_of_class(obj, a_class):
    """ Returns boolean if obj is instance of or inherits from a_class """
    return isinstance(obj, a_class)
