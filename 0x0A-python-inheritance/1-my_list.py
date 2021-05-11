#!/usr/bin/python3

"""
Module that defines MyList class
"""


class MyList(list):
    """ Defines attributes and methods of class that inherits from list """

    def print_sorted(self):
        """ Method to print MyList ints in ascending order """
        print(sorted(self))
