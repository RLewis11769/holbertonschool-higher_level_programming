#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = len(sys.argv)
    sum = 0
    for x in range(1, num):
        sum += int(sys.argv[x])
    print("{}".format(sum))
