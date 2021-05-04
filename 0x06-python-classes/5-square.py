#!/usr/bin/python3

""" Module that defines square """


class Square:
    """ Represents class defining Square parameters """
    def __init__(self, size=0):
        """ Method that initializes size """
        self.__size = size

    @property
    def size(self):
        """ Getter method to set private attributes with better readability """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter method to set size and raise exceptions """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Method that calculates area by area by base * height of square """
        area = self.__size * self.__size
        return area

    def my_print(self):
        """ Method to print square defined in class """
        if self.size == 0:
            print()
        for down in range(self.size):
            for across in range(self.size):
                print("#", end="")
            print()
