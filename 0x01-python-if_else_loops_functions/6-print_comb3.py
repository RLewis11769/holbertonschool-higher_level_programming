#!/usr/bin/python3
for first in range(0, 10):
    for second in range(0, 10):
        if first < second:
            print("{}{}".format(first, second), end='')
            if first != 8:
                print(", ", end='')
            else:
                print()
