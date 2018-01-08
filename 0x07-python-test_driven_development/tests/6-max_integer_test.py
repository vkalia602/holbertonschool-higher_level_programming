#!/usr/bin/python3
"""Module to test code for module- Find max integer
"""


import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test1(self):
        """test a list of ints
        return: 4
        """
        list1 = [1, 2, 8, 4, 6]
        self.assertEqual(max_integer(list1), 8)

    def test2(self):
        """ tests a tuple
        return: TypeError
        """
        list1 = (8, 3, 4)
        with self.assertRaises(TypeError):
            max_integer(list1)

    def test3(self):
        """tests string in list
        expected return: TypeError
        """
        list1 = ["Hello", 5, 6, 8, 9]
        with self.assertRaises(TypeError):
            max_integer(list1)

    def test4(self):
        """ tests for empty list
        expected return: None
        """
        list1 = []
        with self.assertRaises(TypeError):
            max_integer(list1)

    def test5(self):
        """tests when list = None
        expected return: TypeError
        """
        list1 = None
        with self.assertRaises(TypeError):
            max_integer(list1)

    def test5(self):
        """tests when list = None
        expected return: TypeError
        """
        with self.assertRaises(TypeError):
            max_integer("this string")

    def test6(self):
        """tests for list with negative numbers
        expected return: TypeError
        """
        list1 = [-2, -5, -8, -9]
        self.assertEqual(max_integer(list1), -2)

if __name__ == '__main__':
    unittest.main()
