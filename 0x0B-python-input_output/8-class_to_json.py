#!/usr/bin/python3

"""
class_to_json - returns dictionary description for JSON object
@obj: JSON object to find dict of
Return: dictionary description for obj
"""


def class_to_json(obj):
    """  Finds dict for obj """
    return obj.__dict__
