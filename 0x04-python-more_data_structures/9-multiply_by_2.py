#!/usr/bin/python3
def multiply_by_2(a_dictionary):
        times_two = {}
        for key, value in a_dictionary.items():
                times_two[key] = value * 2
        return times_two
