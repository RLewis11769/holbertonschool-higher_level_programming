#!/usr/bin/python3

"""
read_file - reads text file and prints to stdout
@filename - text file to read from
"""


def read_file(filename=""):
    """ prints filename to stdout """
    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end="")
