#!/usr/bin/python3

""" Unit tests for rectangle.py """


import unittest
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """ Test cases for base.py """

    def test_attributes(self):
        """ Tests for proper attribute assignment """
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 5)
        r2 = Rectangle(2, 2)
        self.assertEqual(r2.id, 7)

    def test_validator_hw_errors(self):
        """ Tests with incorrect width/height input """
        with self.assertRaises(TypeError):
            Rectangle(5.3, 9)
        with self.assertRaises(ValueError):
            Rectangle(-3, 7)
        with self.assertRaises(ValueError):
            Rectangle(800, 0)
        with self.assertRaises(TypeError):
            Rectangle(3, "str")
        with self.assertRaises(ValueError):
            Rectangle(2, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, -9)

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

    def test_area(self):
        """ Tests for area method """
        r3 = Rectangle(2, 2)
        self.assertEqual(r3.area(), 4)
        r4 = Rectangle(10, 10)
        self.assertEqual(r4.area(), 100)

    def test_str(self):
        """ Tests for __str__ method """
        r5 = Rectangle(5, 5, 10, 10, 1)
        self.assertEqual(str(r5), "[Rectangle] (1) 10/10 - 5/5")
        r6 = Rectangle(2, 7)
        self.assertEqual(str(r6), "[Rectangle] (8) 0/0 - 2/7")

if __name__ == '__main__':
    unittest.main()
