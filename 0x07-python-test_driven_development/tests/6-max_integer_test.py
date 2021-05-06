#!/usr/bin/python3

""" Unittest for max_integer([..]) """


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ Create test cases for 6-max_integer.py """

    def test_true_pos(self):
        """ Test cases where max is positive number """
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)
        self.assertEqual(max_integer([1, 3, 5, 2, 4]), 5)
        self.assertEqual(max_integer([1000, 750, 999999]), 999999)

    def test_true_other(self):
        """ Test cases where max is negative """
        self.assertEqual(max_integer([-7, -6, -5]), -5)
        self.assertEqual(max_integer([-10, 1, 2, 3]), 3)
        self.assertEqual(max_integer([0, 3, -7]), 3)

    def same(self):
        """ Test cases with identical numbers at some point """
        self.assertEqual(max_integer([3, 3, 3, 5]), 5)
        self.assertEqual(max_integer([5, 5, 3, 5]), 5)
        self.assertEqual(max_integer([-1, -1, -1, -5]), -1)

    def raises(self):
        """ Test cases with incorrect type input """
        self.assertRaises(TypeError, max_integer("String"))
        self.assertRaises(TypeError, max_integer((1, 2)))
        self.assertRaises(TypeError, max_integer([1, 2.5]))

    def other(self):
        """ Test cases where tests are not grouped """
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([3]), 3)
