#!/usr/bin/python3

""" Module that defines Rectangle class (inherits from Base) """


from models.base import Base


class Rectangle(Base):
    """ Defines attributes and methods of Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Instantiates all attributes of class """
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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Gets private height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets height attribute with exceptions """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ Gets private x attribute """
        return self.__x

    @x.setter
    def x(self, value):
        """ Sets x attribute with exceptions """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ Gets private y attribute """
        return self.__y

    @y.setter
    def y(self, value):
        """ Sets y attribute with exceptions """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
