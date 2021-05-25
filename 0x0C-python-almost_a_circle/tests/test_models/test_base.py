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
        b4 = Base()
        b5 = Base(15)
        b6 = Base()
        self.assertEqual(b6.id, 4)

    def test_from_json(self):
        """ Tests for from_json_string method """
        obj = Base.from_json_string("[]")
        self.assertEqual(obj, [])
        obj2 = Base.from_json_string(None)
        self.assertEqual(obj, [])

    def test_to_json(self):
        """ Test for to_json_string method """
        jason = Base.to_json_string([])
        self.assertEqual(jason, "[]")
        jason = Base.to_json_string(None)
        self.assertEqual(jason, "[]")

if __name__ == '__main__':
    unittest.main()
