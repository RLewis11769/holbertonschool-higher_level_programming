#!/usr/bin/python3

""" Module that defines locked class """


class LockedClass:
    """
    Locked class with explicitly-stated instance attributes
    Prevents user from creating instance attributes other than "first_name"
    Faster access, uses less memory, stores values in slots instead of dict
    """
    __slots__ = "first_name"
