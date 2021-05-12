#!/usr/bin/python3

"""
from_json_string - returns object represented by JSON object
@my_str: JSON string to find string of
"""


import json


def from_json_string(my_str):
    """ finds string representation of my_str (JSON object) """
    str = json.loads(my_str)
    return str
