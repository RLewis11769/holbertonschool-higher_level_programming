#!/usr/bin/python3

"""
safe_print_list - prints x number of a list
@my_list - list of any type
@x - number of elements to print
Returns: number of elements printed
"""
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for val in range(x):
            print("{}".format(my_list[val]), end="")
            count += 1
        print()
        return count
    except IndexError:
        print()
        return count
