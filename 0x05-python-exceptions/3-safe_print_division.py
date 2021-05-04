#!/usr/bin/python3

"""
safe_print_list_division - prints result of division
a - first integer (to be divided)
b - second integer (to divide)
Return: result of division
"""


def safe_print_division(a, b):
    try:
        div = a / b
    except:
        div = None
    finally:
        print("Inside result: {}".format(div))
        return div
