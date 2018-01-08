#!/usr/bin/python3
"""Module to test code for module- Find max integer
"""
import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test1(self):
        list1 = [1, 2, 8, 4, 6]
        self.assertEqual(max_integer(list1), 8)

    def test2(self):
        list1 = ("HELLO", 3, 4)
        with self.assertRaises(TypeError)
