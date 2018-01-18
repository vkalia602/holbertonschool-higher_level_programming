#!/usr/bin/python3
"""
function that Creates an Object from a “JSON file”


"""


import json


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file”

    Args:
        filename: name of the JSON file
    """
    with open(filename, mode="r", encoding="utf-8") as my_file:
        return json.load(my_file)
