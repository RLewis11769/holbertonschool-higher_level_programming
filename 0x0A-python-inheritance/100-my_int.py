#!/usr/bin/python3

""" Module that defines MyInt class """


class MyInt(int):
    """ Defines methods and attributes of MyInt class """

    def __init__(self, operator):
        """ Instantiates operator attribute """
        self.operator = operator

    def __eq__(self, other):
        """ Method that defines == as opposite """
        if self.operator is other:
            return False
        return not other

    def __ne__(self, other):
        """ Method that defines != as opposite """
        return not self.__eq__(other)
