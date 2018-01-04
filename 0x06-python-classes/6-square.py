#!/usr/bin/python3
class Square:
    """Class Square initiated by size"""
    def __init__(self, size=0, position=(0, 0)):
        """Args:
        size (int): Size of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
            return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return (self.size ** 2)

    def my_print(self):
        if self.size == 0:
            print("")
        else:
            if self.position[1] > 0:
                for j in range(self.position[1]):
                    print()
            for i in range(self.size):
                if self.position[0] > 0:
                    print(" " * self.position[0], end="")
                print("#" * self.size)
