#!/usr/bin/python3

"""
safe_print_integer - prints integer
@value: any type (integers printed, others raise error)
Return: True if integer, False if not
"""

import sys

def safe_print_integer_err(value):
    """ Regardless of input, prints integers not other types """
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        """ if exception, prints message from stderr to stdout """
        print("Exception: {}".format(e), file=sys.stderr)
        return False
