#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_correct(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_type(self):
        self.assertEqual(max_integer("123"), "3")
        self.assertRaises(TypeError, max_integer, 1)
        self.assertRaises(TypeError, max_integer, True)
        self.assertEqual(max_integer({}), None)
        self.assertRaises(KeyError, max_integer, {"name": "Josh"})

    def test_argument(self):
        self.assertEqual(max_integer(), None)
        self.assertRaises(TypeError, max_integer, 1, 2, 3)
        self.assertRaises(TypeError, max_integer, 1)
