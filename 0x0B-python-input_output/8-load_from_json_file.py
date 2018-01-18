#!/usr/bin/python3


import json


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file”

    Args:
        filename: name of the JSON file
    """
    with open(filename, encoding="UTF-8") as my_file:
        return json.load(my_file)
