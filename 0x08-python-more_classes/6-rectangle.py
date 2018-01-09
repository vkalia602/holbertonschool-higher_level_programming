#!/usr/bin/python3
class Rectangle:
    """Class Rectangle instantiated by width

    Args:
    width(int) - Width of the rectangle
    height(int) - height of the rectangle
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return (self.height + self.width) * 2

    def __str__(self):
        new_string = ""
        if self.height == 0 and self.width == 0:
            return new_string

        for idx in range(self.height):
            for idx2 in range(self.width):
                new_string += '#'
            if idx < self.height - 1:
                new_string += '\n'
        return new_string

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
