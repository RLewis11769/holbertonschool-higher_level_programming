#!/usr/bin/python3

""" Unit tests for rectangle.py """


import unittest
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """ Test cases for base.py """

    def test_attributes(self):
        """ Tests for proper attribute assignment """
        r1 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 1)

    def test_validator_hw_errors(self):
        """ Tests with incorrect width/height input """
        with self.assertRaises(TypeError):
            Rectangle(5.3, 9)
        with self.assertRaises(ValueError):
            Rectangle(-3, 7)
        with self.assertRaises(TypeError):
            Rectangle(3, "str")
        with self.assertRaises(ValueError):
            Rectangle(2, 0)

    def test_validator_xy_errors(self):
        """ Tests with incorrect x/y input """
        with self.assertRaises(TypeError):
            Rectangle(1, 2, (3, 4))
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(TypeError):
            Rectangle(2, 4, 0, [34])
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 89, -1)

if __name__ == '__main__':
    unittest.main()
