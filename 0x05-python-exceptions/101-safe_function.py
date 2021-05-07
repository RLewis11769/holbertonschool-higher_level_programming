#!/usr/bin/python3

"""
safe_function - executes any function
@fct: pointer to function to execute
@args: 2d array of arguments to function
Return: ideally return of function, otherwise None
"""

import sys


def safe_function(fct, *args):
    """ Attempts to return result of function with args passed in """
    try:
        return fct(*args)
    except Exception as e:
        """ if exception, prints message from stderr to stdout """
        print("Exception: {}".format(e), file=sys.stderr)
        return None
