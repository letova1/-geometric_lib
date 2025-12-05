import unittest
from rectangle import*
class RectangleTest(unittest.TestCase):
    def test_zero(self):
        res1=area(10,0)
        self.assertEqual(res1,0)
        res2 = area(0, 10)
        self.assertEqual(res2,0)

    def test_square(self):
        res=area(10, 10)
        self.assertEqual(res, 100)
    def test_perimetr(self):
        res=perimetr(10,10)
        self.assertEqual(res, 40)

    def test_negative(self):
        with self.assertRaises(ValueError):
            area(-10,5)
        with self.assertRaises(ValueError):
            area(10,-5)
        with self.assertRaises(ValueError):
            perimetr(10,-5)
        with self.assertRaises(ValueError):
            perimetr(-10,5)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            area("10",5)
        with self.assertRaises(TypeError):
            area(10,"5")
        with self.assertRaises(TypeError):
            perimetr(10,"5")
        with self.assertRaises(TypeError):
            perimetr("10",5)
