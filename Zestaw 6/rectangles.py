from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return f"[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y})]"  # "[(x1, y1), (x2, y2)]"

    def __repr__(self):
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"  # "Rectangle(x1, y1, x2, y2)"

    def __eq__(self, other):
        return self.pt1 == other.pt1 and self.pt2 == other.pt2  # obsługa rect1 == rect2

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):
        x = (self.pt1.x + self.pt2.x) / 2
        y = (self.pt1.y + self.pt2.y) / 2
        return Point(x, y)  # zwraca środek prostokąta

    def area(self):
        length = abs(self.pt1.x - self.pt2.x)
        width = abs(self.pt1.y - self.pt2.y)
        return length * width    # pole powierzchni

    def move(self, x, y):
        self.pt1.x += x
        self.pt1.y += y
        self.pt2.x += x
        self.pt2.y += y
        # przesunięcie o (x, y)

# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase):
    def test_str(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(str(rect), "[(1, 2), (3, 4)]")

    def test_repr(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(repr(rect), "Rectangle(1, 2, 3, 4)")

    def test_eq(self):
        rect1 = Rectangle(1, 2, 3, 4)
        rect2 = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect1, rect2)

    def test_ne(self):
        rect1 = Rectangle(1, 2, 3, 4)
        rect2 = Rectangle(5, 6, 7, 8)
        self.assertNotEqual(rect1, rect2)

    def test_center(self):
        rect = Rectangle(0, 0, 4, 4)
        self.assertEqual(rect.center(), Point(2, 2))

    def test_area(self):
        rect = Rectangle(0, 0, 4, 4)
        self.assertEqual(rect.area(), 16)

    def test_move(self):
        rect = Rectangle(1, 2, 3, 4)
        rect.move(1, 1)
        self.assertEqual(rect, Rectangle(2, 3, 4, 5))

if __name__ == '__main__':
    unittest.main()