#!/usr/bin/python3

"""
Module for Base class
"""


import json


class Base:
    """
    class Base
    Args:
        nb_objects - Keep track of instances
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        instantiation of Base class
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) is 0:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            return []
        my_file = "{}.json".format(cls.__name__)
        jstring = ""
        for elements in list_objs:
            my_dict = cls.to_dictionary(elements)
            jstring += (Base.to_json_string(my_dict))
            jstring += ", "
        with open(my_file, "w") as my_file:
            my_file.write(jstring)

    @staticmethod
    def from_json_string(json_string):
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ is "Rectangle":
            ins1 = Rectangle(1, 1)
        if cls.__name__ is "Square":
            ins1 = Square.update(1)
        ins1.update(**dictionary)
        return ins1
