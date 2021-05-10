#!/usr/bin/python3

"""
copy_list - copies one list into another without aliasing
@l: list to copy into new list
"""


def copy_list(l):
    """ copies l into new list (not specified with new variable name) """
    return l.copy()
