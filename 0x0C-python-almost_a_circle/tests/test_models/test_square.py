#!/usr/bin/python3
"""
Module for testing square class
"""

import unittest
import json
import io
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Testrectangle(unittest.TestCase):

    """
    Tests for values set for x, y, width, height
    setter and getter methods for variables
    """

    def test_set_values(self):
        """base test for creating rectangle
        """
        Base._Base__nb_objects = 0
        r1 = Square(10)
        self.assertEqual(1, r1.id)

    def test_set_neg_values(self):
        """base test for creating rectangle
        """
        with self.assertRaises(ValueError) as error:
            r1 = Square(-10)
        self.assertEqual(str(error.exception), "width must be > 0")

    def test_set_values_2(self):
        """all values input in the rectangle
        """
        r1 = Square(10, 0, 0, 12)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 12)

    def test_set_values_3(self):
        """pass in non int values
        """
        with self.assertRaises(TypeError) as error:
            Square("hello", "world", "Hello", "world")
        self.assertEqual(str(error.exception), "width must be an integer")

    def test_set_values_4(self):
        """send in a list of ints
        """
        with self.assertRaises(TypeError) as error:
            Square([1, 2, 3, 4, 5])
        self.assertEqual(str(error.exception), "width must be an integer")

    def test_set_values_5(self):
        """x must be an integer
        """
        with self.assertRaises(TypeError) as error:
            Square(1, "Hello", 5, 6)
        self.assertEqual(str(error.exception), "x must be an integer")

    def test_set_values_6(self):
        """y must be an integer
        """
        with self.assertRaises(TypeError) as error:
            Square(1, 3, "Hello", 3)
        self.assertEqual(str(error.exception), "y must be an integer")

    def test_set_values_7(self):
        """test for negative number for width
        """
        with self.assertRaises(ValueError) as error:
            Square(-1, 3, 4, 5)
        self.assertEqual(str(error.exception), "width must be > 0")

    def test_set_values_8(self):
        """test for negative number for x
        """
        with self.assertRaises(ValueError) as error:
            Square(1, -3, 4, 5)
        self.assertEqual(str(error.exception), "x must be >= 0")

    def test_set_values_9(self):
        """test for negative number for y
        """
        with self.assertRaises(ValueError) as error:
            Square(2, 3, -4, 5)
        self.assertEqual(str(error.exception), "y must be >= 0")

    def test_set_values_10(self):
        """test for floats- width
        """
        with self.assertRaises(TypeError) as error:
            Square(1.3, 3, 2, 3)
        self.assertEqual(str(error.exception), "width must be an integer")

    def test_set_values_11(self):
        """test for floats- y
        """
        with self.assertRaises(TypeError) as error:
            Square(1, 3, 2.3, 3)
        self.assertEqual(str(error.exception), "y must be an integer")

    def test_set_values_12(self):
        """test for floats - x
        """
        with self.assertRaises(TypeError) as error:
            Square(1, 3.3, 2, 3)
        self.assertEqual(str(error.exception), "x must be an integer")

    def test_set_values_13(self):
        """pass no arguments for height and width
        """
        with self.assertRaises(TypeError):
            r = Square()

    def test_area_14(self):
        """ Base test for area of rectangle
        """
        r1 = Square(3)
        self.assertEqual(r1.area(), 9)

    def test_area_15(self):
        """test area for
        """
        r1 = Square(9, 3, 4, 2)
        self.assertEqual(r1.area(), 81)

    def test_display_16(self):
        """passing base argument size
        """
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r1 = Square(2)
        r1.display()
        dis_string = "##\n##\n"
        self.assertEqual(capturedOutput.getvalue(), dis_string)

    def test_display_17(self):
        """passing arguments for side, x, y
        """
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r1 = Square(2, 4, 1)
        r1.display()
        dis_string = "\n    ##\n    ##\n"
        self.assertEqual(capturedOutput.getvalue(), dis_string)

    def test_string_18(self):
        """test string with id, width, height, x, y
        """

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        string = "[Square] (12) 2/1 - 4\n"
        r1 = Square(4, 2, 1, 12)
        print(r1)
        self.assertEqual(capturedOutput.getvalue(), string)

    def test_args_kwargs_19(self):
        """test to update id field
        """
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r1 = Square(10, 10, 10, 10)
        r1.update(89)
        string = "[Square] (89) 10/10 - 10\n"
        print(r1)
        self.assertEqual(capturedOutput.getvalue(), string)

    def test_args_kwargs_20(self):
        """passing more arguments than acceptable range
        """
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r1 = Square(10, 10, 10, 10)
        r1.update(1, 2, 3, 4, 5, 6, 6, 4)
        string = "[Square] (1) 3/4 - 2\n"
        print(r1)
        self.assertEqual(capturedOutput.getvalue(), string)

    def test_args_kwargs_21(self):
        """passing kwargs for height, width and x
        """
        Base._Base__nb_objects = 0
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r1 = Square(10, 10, 10, 10)
        r1.update(size=1, x=2)
        string = "[Square] (10) 2/10 - 1\n"
        print(r1)
        self.assertEqual(capturedOutput.getvalue(), string)

    def test_args_kwargs_22(self):
        """passing kwargs for height, width, x, y, id
        """
        Base._Base__nb_objects = 0
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r1 = Square(10, 10, 10, 10)
        r1.update(size=2, x=2, id=4, y=8)
        string = "[Square] (4) 2/8 - 2\n"
        print(r1)
        self.assertEqual(capturedOutput.getvalue(), string)

    def test_args_kwargs_23(self):
        """passing args and kwargs at the same time"""
        Base._Base__nb_objects = 0
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r1 = Square(10, 10, 10, 10)
        r1.update(3, 4, size=4, x=2)
        string = "[Square] (3) 10/10 - 4\n"
        print(r1)
        self.assertEqual(capturedOutput.getvalue(), string)

    def test_to_dict24(self):
        """base case to check for dictionary
        """
        Base._Base__nb_objects = 0
        r1 = Square(10, 10, 10, 10)
        my_dict = r1.to_dictionary()
        dict_out = {'x': 10, 'y': 10, 'id': 1, 'size': 10}
        self.assertEqual(my_dict, dict_out)

    def test_to_dict24(self):
        """dictionary check
        """
        Base._Base__nb_objects = 0
        r1 = Square(10, 10, 10, 10)
        my_dict = r1.to_dictionary()
        dict_out = {'x': 10, 'y': 10, 'id': 10, 'size': 10}
        self.assertEqual(my_dict, dict_out)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(type(my_dict))
        self.assertEqual(capturedOutput.getvalue(), "<class 'dict'>\n")

if __name__ == '__main__':
    unittest.main()
