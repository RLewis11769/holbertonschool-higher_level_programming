#!/usr/bin/python3

""" Base module -- manage id attribute and avoid duplicating code """


import json


class Base:
    """ Defines attributes and methods of Base class """

    """ Class attributes """
    """ Counts number of non-specified ids """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Instantiates public id attribute """
        if id is not None and id <= Base.__nb_objects:
            raise ValueError("Please choose different id")
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ Returns json string of dictionary """
        if list_dictionaries is None:
            return "[]"
        if list_dictionaries == "[]":
            return "[]"
        jsonStr = json.dumps(list_dictionaries)
        return jsonStr
