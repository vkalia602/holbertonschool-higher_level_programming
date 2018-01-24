#!/usr/bin/python3


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
        """base test for creating rectangle"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 2)
        self.assertEqual(1, r1.id)

    def test_set_values_2(self):
        """all values input in the rectangle"""
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 12)

    def test_set_values_3(self):
        """pass in non int values"""
        with self.assertRaises(TypeError) as error:
            Rectangle(10, "hello", "world", "Hello", "world")
        self.assertEqual(str(error.exception), "height must be an integer")

    def test_set_values_4(self):
        """send in a list of ints"""
        with self.assertRaises(TypeError) as error:
            Rectangle([1, 2, 3, 4, 5], 3)
        self.assertEqual(str(error.exception), "width must be an integer")

    def test_set_values_5(self):
        """x must be an integer"""
        with self.assertRaises(TypeError) as error:
            Rectangle(1, 3, "Hello", 5, 6)
        self.assertEqual(str(error.exception), "x must be an integer")

    def test_set_values_6(self):
        """y must be an integer"""
        with self.assertRaises(TypeError) as error:
            Rectangle(1, 2, 3, "Hello", 3)
        self.assertEqual(str(error.exception), "y must be an integer")

    def test_set_values_7(self):
        """test for negative number for width"""
        with self.assertRaises(ValueError) as error:
            Rectangle(-1, 2, 3, 4, 5)
        self.assertEqual(str(error.exception), "width must be > 0")

    def test_set_values_8(self):
        """test for negative number for height"""
        with self.assertRaises(ValueError) as error:
            Rectangle(1, -2, 3, 4, 5)
        self.assertEqual(str(error.exception), "height must be > 0")

    def test_set_values_9(self):
        """test for negative number for x"""
        with self.assertRaises(ValueError) as error:
            Rectangle(1, 2, -3, 4, 5)
        self.assertEqual(str(error.exception), "x must be >= 0")

    def test_set_values_10(self):
        """test for negative number for y"""
        with self.assertRaises(ValueError) as error:
            Rectangle(1, 2, 3, -4, 5)
        self.assertEqual(str(error.exception), "y must be >= 0")

    def test_set_values_11(self):
        """test for floats- width"""
        with self.assertRaises(TypeError) as error:
            Rectangle(1.3, 2, 3, 2, 3)
        self.assertEqual(str(error.exception), "width must be an integer")

    def test_set_values_12(self):
        """test for floats - height"""
        with self.assertRaises(TypeError) as error:
            Rectangle(1, 3.3, 3, 2, 3)
        self.assertEqual(str(error.exception), "height must be an integer")

    def test_set_values_13(self):
        """test for floats- y"""
        with self.assertRaises(TypeError) as error:
            Rectangle(1, 2, 3, 2.3, 3)
        self.assertEqual(str(error.exception), "y must be an integer")

    def test_set_values_14(self):
        """test for floats - x"""
        with self.assertRaises(TypeError) as error:
            Rectangle(1, 2, 3.3, 2, 3)
        self.assertEqual(str(error.exception), "x must be an integer")

    def test_set_values_15(self):
        """pass no arguments for height and width"""
        with self.assertRaises(TypeError):
            r = Rectangle()
        with self.assertRaises(TypeError):
            r = Rectangle(1,)

    """
    Tests for the area method
    """

    def test_area_16(self):
        """ Base test for area of rectangle"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

    def test_area_17(self):
        """test area for """
        r1 = Rectangle(8, 9, 3, 4, 2)
        self.assertEqual(r1.area(), 72)

    """
    Tests for display method
    """

    def test_display_16(self):
        """passing base argument height and width"""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r1 = Rectangle(2, 2)
        r1.display()
        dis_string = "##\n##\n"
        self.assertEqual(capturedOutput.getvalue(), dis_string)

    def test_display_17(self):
        """passing arguments for height, width, x, y"""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r1 = Rectangle(2, 2, 4, 1)
        r1.display()
        dis_string = "\n    ##\n    ##\n"
        self.assertEqual(capturedOutput.getvalue(), dis_string)

    """
    test __str__ method
    """

    def test_string_18(self):
        """test string with id, width, height, x, y"""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        string = "[Rectangle] (12) 2/1 - 4/6\n"
        r1 = Rectangle(4, 6, 2, 1, 12)
        print(r1)
        self.assertEqual(capturedOutput.getvalue(), string)

    """
    test update method for args and kwargs
    """
    def test_args_kwargs_19(self):
        """test to update id field"""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        string = "[Rectangle] (89) 10/10 - 10/10\n"
        print(r1)
        self.assertEqual(capturedOutput.getvalue(), string)

    def test_args_kwargs_20(self):
        """passing more arguments than acceptable range"""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(1, 2, 3, 4, 5, 6, 6, 4)
        string = "[Rectangle] (1) 4/5 - 2/3\n"
        print(r1)
        self.assertEqual(capturedOutput.getvalue(), string)

    def test_args_kwargs_21(self):
        """passing kwargs for height, width and x"""
        Base._Base__nb_objects = 0
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1, width=1, x=2)
        string = "[Rectangle] (1) 2/10 - 1/1\n"
        print(r1)
        self.assertEqual(capturedOutput.getvalue(), string)

    def test_args_kwargs_22(self):
        """passing kwargs for height, width, x, y, id"""
        Base._Base__nb_objects = 0
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1, width=1, x=2, id=4, y=8)
        string = "[Rectangle] (4) 2/8 - 1/1\n"
        print(r1)
        self.assertEqual(capturedOutput.getvalue(), string)

    def test_args_kwargs_23(self):
        """passing args and kwargs at the same time"""
        Base._Base__nb_objects = 0
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(3, 4, height=4, x=2)
        string = "[Rectangle] (3) 10/10 - 4/10\n"
        print(r1)
        self.assertEqual(capturedOutput.getvalue(), string)

    """tests for to_dictionary method"""
    def test_to_dict24(self):
        """base case to check for dictionary"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 10, 10, 10)
        my_dict = r1.to_dictionary()
        dict_out = {'x': 10, 'y': 10, 'id': 1, 'height': 10, 'width': 10}
        self.assertEqual(my_dict, dict_out)

    def test_to_dict24(self):
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 10, 10, 10)
        my_dict = r1.to_dictionary()
        dict_out = {'x': 10, 'y': 10, 'id': 1, 'height': 10, 'width': 10}
        self.assertEqual(my_dict, dict_out)
