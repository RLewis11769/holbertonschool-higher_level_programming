#!/usr/bin/python3

""" Module that defines Rectangle class (inherits from Base) """


from models.base import Base


class Rectangle(Base):
    """ Defines attributes and methods of Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Instantiates all attributes of class """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def data_validator(self, name, value):
        """ Validates proper integer input """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if name == "height" or name == "width":
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        else:
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """ Calculates area """
        return self.width * self.height

    def display(self):
        """ Prints rectangle instance of #s """
        """ Coordinates for position are x-axis (LR) and y-axis (NS) """
        for coordY in range(self.y):
            print()
        for column in range(self.height):
            for coordLR in range(self.x):
                print(" ", end="")
            for row in range(self.width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """ Updates attribute values after initialization """
        arg_name = ['id', 'width', 'height', 'x', 'y']
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
        """ Returns dictionary representation of rectangle """
        dict_rect = {}
        dict_rect["id"] = self.id
        dict_rect["width"] = self.width
        dict_rect["height"] = self.height
        dict_rect["x"] = self.x
        dict_rect["y"] = self.y
        return dict_rect

    def __str__(self):
        """ Builtin that produces readable output """
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id, self.x, self.y,
                                                self.width, self.height)

    @property
    def width(self):
        """ Gets private width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets width attribute with exceptions """
        self.data_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """ Gets private height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets height attribute with exceptions """
        self.data_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """ Gets private x attribute """
        return self.__x

    @x.setter
    def x(self, value):
        """ Sets x attribute with exceptions """
        self.data_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """ Gets private y attribute """
        return self.__y

    @y.setter
    def y(self, value):
        """ Sets y attribute with exceptions """
        self.data_validator("y", value)
        self.__y = value
