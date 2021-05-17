#!/usr/bin/python3

""" Base module -- manage id attribute and avoid duplicating code """


import json


class Base:

    """ Defines attributes and methods of Base class """

    """ Class attributes """
    """ Counts number of non-specified ids """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Instantiates public id attribute - not identical """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def from_json_string(json_string):
        """ Returns list from json string """
        if json_string is None:
            return []
        if json_string == "[]":
            return []
        list_str = json.loads(json_string)
        return list_str

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns json string from dictionary """
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

    @classmethod
    def create(cls, **dictionary):
        """ Creates instance with attributes set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        """ Updates file based on dictionary value """
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Returns list of instances """
        filename = cls.__name__ + ".json"
        instance_list = []
        try:
            """ Read from file (in json format) """
            with open(filename) as jsonFile:
                jsonStr = jsonFile.read()
            """ Convert json string into list """
            new_list = cls.from_json_string(jsonStr)
            for instance in new_list:
                """ Convert each list item to dict """
                instance_dict = dict(instance)
                """ Create new instance based on dict """
                instance_create = cls.create(**instance_dict)
                """ Add each instance to list """
                instance_list.append(instance_create)
            return instance_list
        except:
            return instance_list
