#!/usr/bin/python3
"""
function that reads n lines of a text file (UTF8) and prints it to stdout

"""


def read_lines(filename="", nb_lines=0):
    with open(filename, encoding="utf-8") as my_file:
        x = 0
        for line in my_file:
            if x == nb_lines and nb_lines > 0:
                break
            else:
                print(line, end="")
            x += 1
