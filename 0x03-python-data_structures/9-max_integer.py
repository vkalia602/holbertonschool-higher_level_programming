#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    i = 0
    x = my_list[0]
    while (i < (len(my_list))):
        if x < my_list[i]:
            x = my_list[i]
        i = i + 1
    return x
