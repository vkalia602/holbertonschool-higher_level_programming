#!/usr/bin/python3
"""
Subclass of list


"""


class MyList(list):

    def print_sorted(self):
        """
        Method prints a sorted list
        """
        print(sorted(self))
