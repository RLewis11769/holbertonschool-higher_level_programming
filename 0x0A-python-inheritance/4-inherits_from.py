#!/usr/bin/python3

"""
inherits_from - checks if given object is inherits from given class
@obj: object to check
@a_class: class to check if obj inherits from
Return: True or False
"""


def inherits_from(obj, a_class):
    """ Returns boolean if obj inherits from a_class directly or indirectly """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
