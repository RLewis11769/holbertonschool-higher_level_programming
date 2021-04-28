#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = len(sys.argv)
    if num == 1:
        print("0 arguments.")
    else:
        print("{} arguments:".format(num - 1))
        for elem in range(1, num):
            print("{}: {}".format(elem, sys.argv[elem]))
