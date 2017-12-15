#!/usr/bin/python3
def multiply_by_2(my_dict):
    new_dict = dict(my_dict)
    for numb in new_dict:
        new_dict[numb] *= 2
    return new_dict
