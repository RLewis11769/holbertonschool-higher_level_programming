#!/usr/bin/python3

""" Module that defines BaseGeometry class """


class BaseGeometry:
    """ Defines methods and attributes of BaseGeometry class """

    def area(self):
        """ Method that raises exception if area is not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Method that validates proper input """
        """ Name always string, value always int greater than 0 """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
