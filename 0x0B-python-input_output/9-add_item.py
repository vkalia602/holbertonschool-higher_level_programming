#!/usr/bin/python3
"""
script that adds all arguments to a Python list, and then save them to a file

"""

import json
import sys

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

my_list = []
try:
    filename = "add_item.json"
    my_list = load_from_json_file(filename)
except:
    pass

for idx in range(1, len(sys.argv)):
    my_list.append(sys.argv[idx])

save_to_json_file(my_list, filename)
