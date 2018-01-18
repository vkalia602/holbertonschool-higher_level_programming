#!/usr/bin/python3


import json


def load_from_json_file(filename):
    with open(filename, mode="r", encoding="UTF-8") as my_file:
        return json.load(my_file)
