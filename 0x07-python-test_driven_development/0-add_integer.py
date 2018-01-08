#!/usr/bin/python3
"""
Module to add integer


"""


def add_integer(a, b):
    """Function adds 2 integers

    """
# check if a is not int or float
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
# check if b is not an int or float
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
# adding and returning a and b
    return int(a) + int(b)
