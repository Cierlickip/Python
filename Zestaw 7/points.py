class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})" # zwraca string "(x, y)"

    def __repr__(self):
        return f"Point({self.x}, {self.y})" # zwraca string "Point(x, y)"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y # obsługa point1 == point2

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y) # v1 - v2

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y  # v1 * v2, iloczyn skalarny, zwraca liczbę

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5 # długość wektora

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points

import unittest

class TestPoint(unittest.TestCase):
    def test_str(self):
        p = Point(1, 2)
        self.assertEqual(str(p), "(1, 2)")

    def test_repr(self):
        p = Point(1, 2)
        self.assertEqual(repr(p), "Point(1, 2)")

    def test_eq(self):
        p1 = Point(1, 2)
        p2 = Point(1, 2)
        p3 = Point(3, 4)
        self.assertEqual(p1, p2)
        self.assertNotEqual(p1, p3)

    def test_ne(self):
        p1 = Point(1, 2)
        p2 = Point(1, 2)
        p3 = Point(3, 4)
        self.assertFalse(p1 != p2)
        self.assertTrue(p1 != p3)

    def test_add(self):
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        result = p1 + p2
        self.assertEqual(result, Point(4, 6))

    def test_sub(self):
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        result = p1 - p2
        self.assertEqual(result, Point(-2, -2))

    def test_mul(self):
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        result = p1 * p2
        self.assertEqual(result, 11)

    def test_cross(self):
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        result = p1.cross(p2)
        self.assertEqual(result, -2)

    def test_length(self):
        p = Point(3, 4)
        result = p.length()
        self.assertEqual(result, 5.0)

    def test_hash(self):
        p1 = Point(1, 2)
        p2 = Point(1, 2)
        p3 = Point(3, 4)

        self.assertEqual(hash(p1), hash(p2))
        self.assertNotEqual(hash(p1), hash(p3))

if __name__ == '__main__':
    unittest.main()