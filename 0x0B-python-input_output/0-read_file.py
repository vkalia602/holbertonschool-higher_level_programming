#!/usr/bin/python3
"""
function that reads a text file (UTF8) and prints it to stdout

"""


def read_file(filename=""):
    """
    Function reads lines in a file

    Args:
        filename (str): File that needs to be read
    """
    with open(filename, mode="r", encoding="utf-8") as my_file:
            print(my_file.read(), end="")
