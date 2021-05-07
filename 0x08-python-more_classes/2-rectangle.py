#!/usr/bin/python3

""" Module that defines Rectangle class """


class Rectangle:
    """ Defines class with height and width attributes """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter method for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter method for setting width and raising errors """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter method for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter method for setting height and raising errors """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Method to calculate area """
        area = self.height * self.width
        return area

    def perimeter(self):
        """ Method to calculate perimeter """
        if self.height == 0 or self.width == 0:
            return 0
        per = self.height * 2 + self.width * 2
        return per
