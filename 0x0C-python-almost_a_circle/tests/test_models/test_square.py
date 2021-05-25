#!/usr/bin/python3

""" Unit tests for square.py """


import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """ Test cases for square.py """

    def test_attributes(self):
        """ Tests for proper attribute assignment """
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 4)
        s1 = Square(1, 2)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)
        s2 = Square(1, 2, 3)
        self.assertEqual(s2.size, 1)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 3)

    def test_validator_errors(self):
        """ Tests with incorrect input """
        with self.assertRaises(TypeError):
            Square(1, 2, (3, 4))
        with self.assertRaises(ValueError):
            Square(1, 2, -3)
        with self.assertRaises(TypeError):
            Square(2, [34], 4)
        with self.assertRaises(ValueError):
            Square(1, -6, 89)
        with self.assertRaises(TypeError):
            Square("yes", 7, 5)
        with self.assertRaises(ValueError):
            Square(0, 8, 5)
        with self.assertRaises(ValueError):
            Square(-8, 1, 1)

    def test_area(self):
        """ Tests for area method """
        s = Square(2)
        self.assertEqual(s.area(), 4)

    def test_str(self):
        """ Tests for __str__ method """
        s = Square(5, 10, 10, 1)
        self.assertEqual(str(s), "[Square] (1) 10/10 - 5")
        s = Square(2, 0, 0, 14)
        self.assertEqual(str(s), "[Square] (14) 0/0 - 2")

    def test_update(self):
        """ Tests for no-keyword argument update method """
        s = Square(1, 0, 0, 1)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 1")
        s.update(19)
        self.assertEqual(str(s), "[Square] (19) 0/0 - 1")
        s. update(800, 4, 2, 3)
        self.assertEqual(str(s), "[Square] (800) 2/3 - 4")

    def test_update_kwargs(self):
        """ Tests for key-worded argument update method """
        s = Square(1, 0, 0, 1)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 1")
        s.update(size=76)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 76")
        s.update(y=1, id=99, size=8, x=4)
        self.assertEqual(str(s), "[Square] (99) 4/1 - 8")

    def test_dict(self):
        """ Tests for to_dictionary method """
        s = Square(5, 3, 9, 76)
        d = s.to_dictionary()
        self.assertEqual(d, {'x': 3, 'y': 9, 'id': 76, 'size': 5})

if __name__ == '__main__':
    unittest.main()
