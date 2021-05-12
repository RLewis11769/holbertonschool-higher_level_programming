#!/usr/bin/python3

"""
to_json_string - returns JSON representation of string
@my_obj: object/string to find JSON representation of
Return: JSON representation of my_obj (always string type)
"""


import json


def to_json_string(my_obj):
    """ finds JSON representation of my_obj """
    jsonStr = json.dumps(my_obj)
    return jsonStr
