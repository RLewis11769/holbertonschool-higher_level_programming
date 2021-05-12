#!/usr/bin/python3

"""
write_file - writes string to text and returns number of characters written
@filename: text file to write to
@text: string to write to file
Return: number of characters in text string
"""


def write_file(filename="", text=""):
    """ Writes text to filename """
    with open(filename, 'w', encoding='utf-8') as f:
        num = f.write(text)
    return num
