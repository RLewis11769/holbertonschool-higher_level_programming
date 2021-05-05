#!/usr/bin/python3

""" Module that defines square """


class Square:
    """ Represents class defining Square parameters """
    def __init__(self, size=0, position=(0,0)):
        """ Method that initializes size """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ Getter method to set private size attribute """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter method to set size and raise exceptions """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Getter method to set private position attribute """
        return self.__position

    @position.setter
    def position(self, value):
        """ Setter method to set position tuple and raise exception """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance (value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Method that calculates area by area by base * height of square """
        area = self.__size * self.__size
        return area

    def my_print(self):
        """ Method to print square defined in class """
        if self.size == 0:
            print()
        for downP in range(self.position[1]):
            print()
        for downS in range(self.size):
            for acrossP in range(self.position[0]):
                print(" ", end="")
            for acrossS in range(self.size):
                print("#", end="")
            print()
