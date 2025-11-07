import unittest
from triangle import*

class TriangleTest(unittest.TestCase):
    def test_area_standard(self):
        res=area(10,6)
        self.assertEqual(res,30)

    def test_perimeter_standard(self):
        res=perimetr(3,4,5)
        self.assertEqual(res,12)

    def test_zero(self):
        res=area(0,0)
        self.assertEqual(res,0)

        res1=perimetr(3,4,0)
        self.assertEqual(res1,7)

    def test_negative_value(self):
        with self.assertRaises(ValueError):
            area(-1,0)
        with self.assertRaises(ValueError):
           perimetr(-1,0,0)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            area("10",5)
        with self.assertRaises(TypeError):
            perimetr(3,4,"5")

