#!/usr/bin/python3

""" Module that defines square """


class Square:
    """ Represents class with private size attribute for each instance """
    def __init__(self, size=0):
        """ Method that raises exceptions and initializes size """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        area = self.__size ** 2
        return area
