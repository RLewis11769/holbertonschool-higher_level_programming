#!/usr/bin/python3

""" Module that defines Rectangle class """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Defines methods and attributes of Rectangle class """
    """ Some methods and attributes inherited from BaseGeometry """

    def __init__(self, width, height):
        """ Instantiates private width and height attributes """
        super().integer_validator("width", width)
        self.__width = width
        BaseGeometry.integer_validator(self, "height", height)
        self.__height = height
