#!/usr/bin/python3
"""
Module with class named Student
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return vars(self)
        my_dict = {}
        new_dict = self.__dict__
        for key, value in new_dict.items():
            if key in attrs:
                my_dict[key] = value
        return my_dict

    def reload_from_json(self, json):
       my_dict = self.__dict__
       for key, value in json.items():
           setattr(self, key, value)
