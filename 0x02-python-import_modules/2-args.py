#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = len(sys.argv)
    if num == 1:
        print("0 arguments.")
    elif num == 2:
        print("{} argument:".format(num - 1))
    else:
        print("{} arguments:".format(num - 1))
    for elem in range(1, num):
        print("{}: {}".format(elem, sys.argv[elem]))
