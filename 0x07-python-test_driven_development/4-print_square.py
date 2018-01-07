#!/usr/bin/python3

"""Prints square with # character"""


def print_square(size):

    errormsg_0 = "size must be an integer"
    errormsg_1 = "size must be >= 0"

# check if size is an integer
    if type(size) is not int:
        raise TypeError(errormsg_0)

# check if size is less than 0
    if size < 0:
        raise ValueError(errormsg_1)

## printing squares
    if size == 0:
        print("")
    for x in range(size):
        print("#" * size)
