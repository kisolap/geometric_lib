import unittest

from rectangle import area
from rectangle import perimeter

class MyTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0, 0)
        self.assertEqual(res, ValueError)

    def test_area_under_zero(self):
        res = area(-3, -2)
        self.assertEqual(res, ValueError)

    def test_area_small_input(self):
        res = area(2, 5)
        self.assertEqual(res, 10)

    def test_area_big_input(self):
        res = area(123456789, 987654321)
        self.assertEqual(res, 121932631112635269)

    def test_perimeter_zero(self):
        res = perimeter(0, 0)
        self.assertEqual(res, ValueError)

    def test_perimeter_small_input(self):
        res = perimeter(2, 5)
        self.assertEqual(res, 14)

    def test_perimeter_big_input(self):
        res = perimeter(123456789, 987654321)
        self.assertEqual(res, 2222222220)

