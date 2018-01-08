#!/usr/bin/python3
"""
This module prints text with blank lines


"""


def text_indentation(text):

    """
    Printing text with 2 new lines after '.' '?' ':' characters

    """
# check if text is string
    if type(text) is not str:
        raise TypeError("text must be a string")
# if an empty string
    if len(text) == 0:
        print("")
# printing text
    symb = ('.', '?', ':')
    index = 0
    while index in range(len(text)):
        if index > 0 and index < len(text) - 1:
            if text[index - 1] in symb and text[index] is " ":
                index += 1
        print("{}".format(text[index]), end="")
        if text[index] in symb:
            print("\n")
        index += 1
