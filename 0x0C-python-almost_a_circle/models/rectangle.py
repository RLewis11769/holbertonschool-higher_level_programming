#!/usr/bin/python3

""" Module that defines Rectangle class (inherits from Base) """


from models.base import Base


class Rectangle(Base):
    """ Defines attributes and methods of Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Instantiates attributes of class """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Gets private width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets width attribute with exceptions """
        if value <= 0:
            raise ValueError("Width must be positive number")
        else:
            self.__width = value

    @property
    def height(self):
        """ Gets private height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets height attribute with exceptions """
        self.__height = value

    @property
    def x(self):
        """ Gets private x attribute """
        return self.__x

    @x.setter
    def x(self, value):
        """ Sets x attribute with exceptions """
        self.__x = value

    @property
    def y(self):
        """ Gets private y attribute """
        return self.__y

    @y.setter
    def y(self, value):
        """ Sets y attribute with exceptions """
        self.__y = value
