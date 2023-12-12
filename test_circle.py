import unittest

from circle import area
from circle import perimeter

class MyTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, ValueError)

    def test_area_under_zero(self):
        res = area(-3)
        self.assertEqual(res, ValueError)

    def test_area_small_input(self):
        res = area(2)
        self.assertEqual(res, 12.566370614359172)

    def test_area_big_input(self):
        res = area(123456789)
        self.assertEqual(res, 4.788283183070884e+16)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, ValueError)

    def test_perimeter_small_input(self):
        res = perimeter(3)
        self.assertEqual(res, 18.84955592153876)

    def test_perimeter_big_input(self):
        res = perimeter(123456789)
        self.assertEqual(res, 775701882.7163703)
