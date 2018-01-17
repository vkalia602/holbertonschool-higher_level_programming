#!/usr/bin/python3
"""
Module that defines BaseGeometry


"""


class BaseGeometry:
    """
    Class Base Geometry


    """

    def __init__(self):
        self.area

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if isinstance(value, int) is not True:
            raise TypeError("must be an integer")
        if value <= 0:
            raise ValueError("must be greater than 0")
