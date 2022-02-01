import unittest
from leap_year import leap_year

class TestLeapYear(unittest.TestCase):
    def test_2000_is_a_leap_year(self):
        self.assertEqual(leap_year(2000), True)

    def test_2009(self):
        self.assertEqual(leap_year(2009), False)

    def test_1700(self):
        self.assertEqual(leap_year(1700), False)

    def test_2004(self):
        self.assertEqual(leap_year(2004), True)