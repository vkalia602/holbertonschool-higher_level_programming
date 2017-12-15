#!/usr/bin/python3
def best_score(my_dict):
    if not my_dict:
        return None
    return max(my_dict.keys())
