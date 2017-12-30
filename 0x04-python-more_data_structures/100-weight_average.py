#!/usr/bin/python3
def weight_average(my_list=[]):
    denom = 0
    add = 0
    for i in range(len(my_list)):
        mult = 1
        for j in range(len(my_list[i])):
            mult *= my_list[i][j]
            if j == 1:
                denom += my_list[i][1]
        add += mult
    if denom == 0:
        return 0
    return add / denom
