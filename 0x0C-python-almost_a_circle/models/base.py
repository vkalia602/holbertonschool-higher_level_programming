#!/usr/bin/python3
"""
Module with class Base
"""

import json
class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        my_file = "{}.json".format(cls.__name__)
        jstring = ""
        for elements in list_objs:
            jstring += Base.to_json_string(elements)
        with open(my_file, "w") as my_file:
            my_file.write(jstring)
