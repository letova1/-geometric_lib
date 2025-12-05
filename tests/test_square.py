import unittest
from square import*

class SquareTest(unittest.TestCase):
    '''тесты, покрывающие корректный результат'''
    def test_area_standard(self):
        res=area(5)
        self.assertEqual(res, 25)
    def test_perimeter_standard(self):
        res=perimeter(5)
        self.assertEqual(res,20)

    '''тесты, покрывающие нуль'''
    def test_zero(self):
        res1=area(0)
        self.assertEqual(res1, 0)
        res2 = perimeter(0)
        self.assertEqual(res2, 0)

    '''тесты, покрывающие невалидные данные (строки и отрицательные числа)'''
    def test_type_error(self):
        with self.assertRaises(TypeError):
            area("5")
        with self.assertRaises(TypeError):
            perimeter("1")

    def test_negative_value_error(self):
        with self.assertRaises(ValueError):
            area(-5)
        with self.assertRaises(ValueError):
            perimeter(-5)



