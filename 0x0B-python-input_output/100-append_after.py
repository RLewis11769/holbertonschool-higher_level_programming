#!/usr/bin/python3

"""
append_after - inserts text to file if line contains string
@filename: file to search and append to
@search_string: if in line, insert text after given line
@new_string: text to insert after found text
"""


def append_after(filename="", search_string="", new_string=""):
    """ Appends new_string to filename after search_string line in filename """
    string = ""
    with open(filename) as f:
        for line in f:
            string += str(line)
            if search_string in line:
                string += new_string

    with open(filename, 'w') as f:
        f.write(string)
