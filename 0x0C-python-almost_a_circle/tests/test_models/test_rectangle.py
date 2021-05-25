#!/usr/bin/python3

""" Unit tests for rectangle.py """


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Test cases for rectangle.py """

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
            Rectangle(0, 800)
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

    def test_update(self):
        """ Tests for no-keyword argument update method """
        r = Rectangle(1, 1, 0, 0, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")
        r.update(19)
        self.assertEqual(str(r), "[Rectangle] (19) 0/0 - 1/1")
        r. update(800, 4, 5, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (800) 2/3 - 4/5")

    def test_update_kwargs(self):
        """ Tests for key-worded argument update method """
        r = Rectangle(1, 1, 0, 0, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")
        r.update(height=76)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/76")
        r.update(y=1, id=99, width=8, x=4)
        self.assertEqual(str(r), "[Rectangle] (99) 4/1 - 8/76")

    def test_dict(self):
        """ Tests for to_dictionary method """
        r = Rectangle(65, 9, 6, 3, 4)
        d = r.to_dictionary()
        self.assertEqual(d, {'x': 6, 'y': 3, 'id': 4, 'height': 9, 'width': 65})

if __name__ == '__main__':
    unittest.main()
