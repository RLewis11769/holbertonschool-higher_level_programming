#!/usr/bin/python3

"""
load_from_json_file - creates object from JSON file
@filename: file to create from (created in 5 in examples given)
Return: object created
"""


import json


def load_from_json_file(filename):
    """  Reads file containing JSON objects and creates objects """
    with open(filename) as jsonFile:
        my_obj = json.load(jsonFile)
    return my_obj
