#!/usr/bin/python3


""" Module that defines Square class (inherits from Rectangle) """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Defines attributes and methods of Square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ Instantiates attributes for Square (from Rectangle) """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ Builtin that produces readable output """
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                                self.id, self.x, self.y,
                                                self.width)

    @property
    def size(self):
        """ Gets private size attribute """
        return self.width

    @size.setter
    def size(self, value):
        """ Sets size attribute from width/height with exceptions """
        self.int_validator("width", value)
        self.value_validator("width", value)
        self.width = value
        self.height = value
