#!/usr/bin/python3

import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Base(unittest.TestCase):

    """
    Tests for id output

    """

    def test_id_type(self):
        """simple initial test"""
        b = Base()
        self.assertEqual(1, b.id)

    def test_id(self):
        """test if the number passed as an argument is the id"""
        b = Base(5)
        self.assertEqual(5, b.id)

    def test_id2(self):
        """test for a string as an argument"""
        b = Base("Hello")
        self.assertEqual("Hello", b.id)

    def test_id3(self):
        """test for a list as an argument"""
        b = Base([1, 2, 3])
        self.assertEqual([1, 2, 3], b.id)

    def test_id4(self):
        """test for a dict passed as an argument"""
        b = Base({"hello":1, "world":2})
        self.assertEqual({"hello":1, "world":2}, b.id)


        """
        Series of tests for @staticmethod that changes dictionary into a
        json string

        """

#    def test_json_dump(self):
 #       r1 = Rectangle(10, 7, 2, 8)
  #      dictionary = r1.to_dictionary()
   #     json_dictionary = Base.to_json_string([dictionary])
    #    jd = [{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]
     #   self.assertEqual(jd, json_dictionary)

