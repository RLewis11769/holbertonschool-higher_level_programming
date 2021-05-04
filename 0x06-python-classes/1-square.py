#!/usr/bin/python3

""" Module that defines square with private attribute """


class Square:
    """ Defines class with size attribute for each instance """
    def __init__(self, size):
        """ Method that defines size for each instance """
        self.__size = size
