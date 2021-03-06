#!/usr/bin/python3

"""
say_my_name - prints name
@first_name: first name string
@last_name: last name string
"""


def say_my_name(first_name, last_name=""):
    """ Function to print introduction when passed name """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
