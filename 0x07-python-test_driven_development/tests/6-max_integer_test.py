#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    class for testing the 6-max-integer
    """
    def test_correct(self):
        """
        test for iteratives
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([7, 2, 3, 4]), 7)
        self.assertEqual(max_integer([1, 5, 3, 4]), 5)
        self.assertEqual(max_integer([4]), 4)

    def test_type(self):
        """
        tests for errors returned from incorrect types
        """
        self.assertEqual(max_integer("123"), "3")
        self.assertRaises(TypeError, max_integer, 1)
        self.assertRaises(TypeError, max_integer, True)
        self.assertEqual(max_integer({}), None)
        self.assertRaises(KeyError, max_integer, {"name": "Josh"})

    def test_argument(self):
        """
        test for the number of arguments provided
        """
        self.assertEqual(max_integer(), None)
        self.assertRaises(TypeError, max_integer, 1, 2, 3)
        self.assertRaises(TypeError, max_integer, 1)
