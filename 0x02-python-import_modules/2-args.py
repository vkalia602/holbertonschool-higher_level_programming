#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    x = len(sys.argv) - 1
    if x is 1:
        print("{:d} argument:".format(x))
        print("{:d}: {}".format(x, sys.argv[x]))
    elif x > 1:
        print("{:d} arguments:".format(x))
        for x in range(1, x + 1):
            print("{:d}: {}".format(x, sys.argv[x]))
    else:
        print("{:d} arguments.".format(x))
