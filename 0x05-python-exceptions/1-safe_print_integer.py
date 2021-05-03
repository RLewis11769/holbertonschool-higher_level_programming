#!/usr/bin/python3

"""
safe_print_integer - prints integer only
value - input of any type
Returns: True if integer
"""
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
