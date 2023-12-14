import unittest

from triangle import area
from triangle import perimeter

class MyTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0, 0)
        self.assertEqual(res, ValueError)

    def test_area_under_zero(self):
        res = area(-3, -1)
        self.assertEqual(res, ValueError)

    def test_area_small_input(self):
        res = area(2, 8)
        self.assertEqual(res, 8.0)

    def test_area_big_input(self):
        res = area(123456789, 987654321)
        self.assertEqual(res, 6.096631555631763e+16)

    def test_perimeter_zero(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, ValueError)

    def test_perimeter_small_input(self):
        res = perimeter(2, 5, 10)
        self.assertEqual(res, 17)

    def test_perimeter_big_input(self):
        res = perimeter(123456789, 987654321, 123456789123456789)
        self.assertEqual(res, 123456790234567899)


