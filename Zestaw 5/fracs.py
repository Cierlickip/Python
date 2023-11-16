#Zadanie 5.2 - Stworzyć plik fracs.py i zapisać w nim funkcje do działań na ułamkach. Ułamek będzie reprezentowany przez listę dwóch liczb całkowitych [licznik, mianownik]. Napisać kod testujący moduł fracs. Nie należy korzystać z klasy Fraction z modułu fractions. Można wykorzystać funkcję fractions.gcd() implementującą algorytm Euklidesa.
import unittest
def add_frac(frac1, frac2):
    result = []
    result.append(frac1[0] * frac2[1] + frac1[1] * frac2[0])
    result.append(frac1[1] * frac2[1])
    return result

def sub_frac(frac1, frac2):
    result = []
    result.append(frac1[0] * frac2[1] - frac1[1] * frac2[0])
    result.append(frac1[1] * frac2[1])
    return result

def mul_frac(frac1, frac2):
    result = []
    result.append(frac1[0] * frac2[0])
    result.append(frac1[1] * frac2[1])
    return result
def div_frac(frac1, frac2):
    result = []
    result.append(frac1[0] * frac2[1])
    result.append(frac1[1] * frac2[0])
    return result
def is_positive(frac):
    num, denom = frac
    return (num > 0 and denom > 0) or (num < 0 and denom < 0)

def is_zero(frac):
    num, _ = frac
    return num == 0

def cmp_frac(frac1, frac2):
    num1, denom1 = frac1
    num2, denom2 = frac2

    product1 = num1 * denom2
    product2 = num2 * denom1

    if product1 < product2:
        return -1
    elif product1 > product2:
        return 1
    else:
        return 0

def frac2float(frac):
    num, den = frac
    return num / den


import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])

    def test_is_positive(self):
        self.assertTrue(is_positive([1, 2]))
        self.assertFalse(is_positive([-1, 2]))

    def test_is_zero(self):
        self.assertTrue(is_zero([0, 1]))
        self.assertFalse(is_zero([1, 2]))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [1, 3]), 1)
        self.assertEqual(cmp_frac([-1, 2], [1, 2]), -1)
        self.assertEqual(cmp_frac([1, 2], [2, 4]), 0)

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 2]), 1/2)
        self.assertEqual(frac2float([-1, 2]), -1/2)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()