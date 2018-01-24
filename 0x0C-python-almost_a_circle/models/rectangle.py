#!/usr/bin/python3
"""
Module with class Base
"""

import sys
from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """
        Method of class Rectangle to calculate the area
        """

        return self.height * self.width

    def display(self):
        """
        method that prints rectangle instance with a character
        """
        for idx in range(self.y):
            print()
        for idx in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        string = ("[Rectangle] ({}) {}/{} - {}/{}".
                  format(self.id, self.x, self.y, self.width, self.height))
        return string

    def update(self, *args, **kwargs):
        if args is None and kwargs is None:
            return
        if len(args) != 0:
            attr_arg = ["id", "width", "height", "x", "y"]
            for idx, arg in enumerate(args):
                if len(attr_arg)  == idx:
                    break
                setattr(self, attr_arg[idx], arg)
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        my_attrs = ["id", "height", "width", "x", "y"]
        my_values = [self.id, self.height, self.width, self.x, self.y]
        my_dict = {}
        my_dict = dict(zip(my_attrs, my_values))
        return my_dict
