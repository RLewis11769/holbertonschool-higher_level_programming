#!/usr/bin/python3

"""
append_write - appends string to file and returns number of characters written
@filename: text file to append/write to
@text: string to append to end of file
Return: number of characters in text string
"""


def append_write(filename="", text=""):
    """ Appends text to end of filename """
    with open(filename, 'a', encoding='utf-8') as f:
        num = f.write(text)
    return num
