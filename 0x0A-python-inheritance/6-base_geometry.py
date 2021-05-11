#!/usr/bin/python3

""" Module that defines BaseGeometry class """


class BaseGeometry:
    """ Defines methods and attributes of BaseGeometry class """

    def area(self):
        """ Method that raises exception if area is not implemented """
        raise Exception("area() is not implemented")
