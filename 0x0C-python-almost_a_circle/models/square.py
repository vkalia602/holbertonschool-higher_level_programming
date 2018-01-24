#!/usr/bin/python3
"""
module square that inherits from class rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square that inherits from Class rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Method initializing arguments

        Args:
            size- size of the square
            x - spaces in the x axis
            y - new lines in the y axis
            id - number of objects
        """
        super().__init__(self.size, self.size, x, y, id)

    def __str__(self):
        p = "[square] ({}) {}/{} - {}".format(self.id, self.x,
                                              self.y, self.size)
        return p

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.height = size
        self.width = size

    def update(self, *args, **kwargs):
        """
        updates the attributes with new values
        """
        if args is None and kwargs is None:
            return
        if len(args) == 0:
            for key in kwargs:
                setattr(self, key, kwargs[key])
        else:
            attr_arg = ["id", "size", "x", "y"]
            for idx, arg in enumerate(args):
                setattr(self, attr_arg[idx], arg)

    def to_dictionary(self):
        """
        creates a dictionary from the attributes and their values
        """
        my_attrs = ["id", "size", "x", "y"]
        my_values = [self.id, self.size, self.x, self.y]
        my_dict = {}
        my_dict = dict(zip(my_attrs, my_values))
        return my_dict
