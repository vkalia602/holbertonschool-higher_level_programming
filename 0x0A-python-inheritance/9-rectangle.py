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
        if type(value) is not int:
            raise TypeError("must be an integer")
        if value <= 0:
            raise ValueError("must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Class Rectangle, subclass of BaseGeometry


    """

    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def print(self):
        print("[Rectangle] {}/{}". format(self.__width, self.__height))

    def __str__(self):
        return "[Rectangle] {}/{}". format(self.__width, self.__height)
