#!/usr/bin/python3

""" Module that defines square """


class Square:
    """ Represents class to define Square parameters """

    def __init__(self, size=0):
        """ Method that raises exceptions and initializes size """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Method to find area of square """
        area = self.__size * self.__size
        return area
