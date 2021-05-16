#!/usr/bin/python3

""" Unit tests for base.py """


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Test cases for base.py """

    def test_id(self):
        """ Tests for proper id assignment """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(7)
        self.assertEqual(b2.id, 7)
        b3 = Base()
        b5 = Base(15)
        b6 = Base()
        self.assertEqual(b6.id, 3)

    def test_id_error(self):
        """ Tests for improper id assignment """
        b1 = Base()
        self.assertEqual(b1.id, 1)

if __name__ == '__main__':
    unittest.main()
