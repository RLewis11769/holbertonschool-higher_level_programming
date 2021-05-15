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

    def update(self, *args, **kwargs):
        """ Updates attribute values """
        arg_name = ['id', 'size', 'x', 'y']
        """ If args only, sets attribute to correct arg_name """
        if len(args) > 0:
            numArgs = 0
            for attr in range(len(args)):
                setattr(self, arg_name[numArgs], args[numArgs])
                numArgs += 1
        """ Put kwargs into dict - if key matches arg_name, set to value """
        kwargs_dict = kwargs
        for key, value in kwargs_dict.items():
            for attr in range(len(arg_name)):
                if key == arg_name[attr]:
                    setattr(self, arg_name[attr], value)

    def to_dictionary(self):
        """ Returns dictionary representation of square """
        dict_sq = {}
        dict_sq["id"] = self.id
        dict_sq["size"] = self.size
        dict_sq["x"] = self.x
        dict_sq["y"] = self.y
        return dict_sq

    @property
    def size(self):
        """ Gets private size attribute """
        return self.width

    @size.setter
    def size(self, value):
        """ Sets size attribute from width/height with exceptions """
        self.data_validator("width", value)
        self.width = value
        self.height = value
