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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns json string of dictionary """
        if list_dictionaries is None:
            return "[]"
        if list_dictionaries == "[]":
            return "[]"
        jsonStr = json.dumps(list_dictionaries)
        return jsonStr

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes json string rep (list_objs) to file """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        obj_list = []
        for instance in list_objs:
            obj_list.append(instance.to_dictionary())
        jsonStr = cls.to_json_string(obj_list)
        with open(filename, 'w') as jsonFile:
            jsonFile.write(jsonStr)
