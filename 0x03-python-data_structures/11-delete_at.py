#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = []
    if idx < 0 or not my_list:
        return None
    elif idx > len(my_list):
        return None
    else:
        del my_list[idx]
    return my_list
