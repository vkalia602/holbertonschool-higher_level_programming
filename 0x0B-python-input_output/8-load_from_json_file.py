#!/usr/bin/python3
"""
Function that creates an Object from a “JSON file”


"""

import json


def load_from_json_file(filename):
    with open(filename, mode="r") as my_file:
        return json.load(my_file)
