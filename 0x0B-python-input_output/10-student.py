#!/usr/bin/python3

""" Module that defines Student class """


class Student:
    """ Defines methods and attributes of Square class """
    def __init__(self, first_name, last_name, age):
        """ Instantiates public first_name, last_name, and age attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns dictionary representation if instance has attribute """
        if type(attrs) is list:
            attr_dict = {}
            for attribute in attrs:
                if hasattr(self, attribute):
                    attr_dict[attribute] = getattr(self, attribute)
            return attr_dict
        return vars(self)
