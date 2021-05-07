#!/usr/bin/python3

""" Module that defines Rectangle class """


class Rectangle:
    """ Defines attributes and methods of class """

    def __init__(self, width=0, height=0):
        """ Initializes each instance of specific rectangle in class """
        self.width = width
        self.height = height

    def __str__(self):
        """ Builtin method for producing readable output """
        rect = ""
        if self.height == 0 or self.width == 0:
                return rect
        for down in range(self. height):
            for across in range(self.width):
                rect += "#"
            if down is not self.height - 1:
                rect += "\n"
        return rect

    def __repr__(self):
        """ Builtin method to print string representation of rect """
        """ Used in conjunction with eval to print """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """ Builtin method to print at every deletion of instance """
        print("Bye rectangle...")

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
        return (self.height * 2) + (self.width * 2)
