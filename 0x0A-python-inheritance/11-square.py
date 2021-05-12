#!/usr/bin/python3

""" Module that defines Square class """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Defines methods and attributes of Square class """
    """ Some methods and attributes inherited from Rectangle """

    def __init__(self, size):
        """ Instantiates private size attribute """
        self.integer_validator("size", size)
        self.__size = size

        """ Implements area method from Rectangle """
        super().__init__(size, size)

    def __str__(self):
        """ Required bc "Rectangle" hardcoded in Rectangle class """
        return "[Square] {}/{}".format(self.__size, self.__size)
