#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
        times_value = map(lambda val: val * number, my_list)
        return list(times_value)
