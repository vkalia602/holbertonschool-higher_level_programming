#!/usr/bin/python3

import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class test_rectangle(unittest.TestCase):

    """
    Tests for values set for x, y, width, height
    """

    def set_values(self):
        """base test for creating rectangle"""
        r1 = Rectangle(10, 2)
        self.assertEqual(1, r1.id)

    def set_values2(self):
        """all values input in the rectangle"""
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 0)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 12)
        self.assertEqual(r1.id, 10)
    def set_values3(self):
        """pass in non int values"""
        with self.assertRaises(TypeError):
            Rectangle(10, "hello", "world", "Hello", "world")
        self.assertEqual(str(err.exception), "width must be an integer")
    def set_values4(self):
        """send in a list of ints"""
        with self.assertRaises(TypeError):
            Rectangle([1, 2, 3, 4, 5])

 #   def set_values5(self):
#        """test height"""
