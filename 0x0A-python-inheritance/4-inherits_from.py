#!/usr/bin/python3
"""
Function that checks for subclass

"""


def inherits_from(obj, a_class):
    return issubclass(type(obj), a_class) and type(obj) != a_class