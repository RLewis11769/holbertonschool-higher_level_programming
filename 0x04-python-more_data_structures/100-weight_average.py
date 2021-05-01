#!/usr/bin/python3
def weight_average(my_list=[]):
        if not my_list or len(my_list) == 0:
                return 0
        total = 0
        div = 0
        for x in my_list:
                total += int(x[0]) * int(x[1])
                div += int(x[1])
        return total / div
