#!/usr/bin/python3
"""
function that reads a text file (UTF8) and prints it to stdout

"""


def read_file(filename=""):
    with open("my_file_0.txt", mode="r", encoding="utf-8") as my_file:
        for line in my_file:
            print(line, end="")
