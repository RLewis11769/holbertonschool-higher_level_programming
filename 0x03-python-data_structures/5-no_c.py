#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for idx in my_string:
        if idx == 'c' or idx == 'C':
            continue
        new = new + idx
    return new
