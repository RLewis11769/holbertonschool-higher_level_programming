#!/usr/bin/python3

"""
save_to_json_file - writes object to text file using JSON rep
@my_obj: object to write to text file
@filename: file to write to
"""


import json


def save_to_json_file(my_obj, filename):
    """  Saves my_obj in filename """
    with open(filename, 'w') as jsonFile:
        jsonFile.write(json.dumps(my_obj))
