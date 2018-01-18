#!/usr/bin/python3
"""
Function that returns the number of lines of a text file

"""


def number_of_lines(filename=""):
    x = 0
    with open(filename) as my_file:
        for line in my_file:
            x += 1
    return x
