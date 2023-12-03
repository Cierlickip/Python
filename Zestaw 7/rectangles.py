#Zadanie 7.3

from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Invalid rectangle coordinates")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return f"[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y})]"

    def __repr__(self):
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"

    def __eq__(self, other):
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):
        return not self == other

    def center(self):
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    def area(self):
        return abs((self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y))

    def move(self, x, y):
        self.pt1.x += x
        self.pt1.y += y
        self.pt2.x += x
        self.pt2.y += y

    def intersection(self, other):
        x_overlap = max(0, min(self.pt2.x, other.pt2.x) - max(self.pt1.x, other.pt1.x))
        y_overlap = max(0, min(self.pt2.y, other.pt2.y) - max(self.pt1.y, other.pt1.y))
        if x_overlap == 0 or y_overlap == 0:
            return None
        else:
            return Rectangle(
                max(self.pt1.x, other.pt1.x),
                max(self.pt1.y, other.pt1.y),
                min(self.pt2.x, other.pt2.x),
                min(self.pt2.y, other.pt2.y)
            )

    def cover(self, other):
        return Rectangle(
            min(self.pt1.x, other.pt1.x),
            min(self.pt1.y, other.pt1.y),
            max(self.pt2.x, other.pt2.x),
            max(self.pt2.y, other.pt2.y)
        )

    def make4(self):
        mid_x = (self.pt1.x + self.pt2.x) / 2
        mid_y = (self.pt1.y + self.pt2.y) / 2

        rect1 = Rectangle(self.pt1.x, self.pt1.y, mid_x, mid_y)
        rect2 = Rectangle(mid_x, self.pt1.y, self.pt2.x, mid_y)
        rect3 = Rectangle(self.pt1.x, mid_y, mid_x, self.pt2.y)
        rect4 = Rectangle(mid_x, mid_y, self.pt2.x, self.pt2.y)

        return rect1, rect2, rect3, rect4


import unittest

class TestRectangle(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(ValueError):
            Rectangle(3, 4, 1, 2)

    def test_str(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(str(rect), "[(1, 2), (3, 4)]")

    def test_repr(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(repr(rect), "Rectangle(1, 2, 3, 4)")

    def test_eq(self):
        rect1 = Rectangle(1, 2, 3, 4)
        rect2 = Rectangle(1, 2, 3, 4)
        rect3 = Rectangle(0, 0, 1, 1)
        self.assertEqual(rect1, rect2)
        self.assertNotEqual(rect1, rect3)

    def test_ne(self):
        rect1 = Rectangle(1, 2, 3, 4)
        rect2 = Rectangle(1, 2, 3, 4)
        rect3 = Rectangle(0, 0, 1, 1)
        self.assertFalse(rect1 != rect2)
        self.assertTrue(rect1 != rect3)

    def test_center(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect.center(), Point(2.0, 3.0))

    def test_area(self):
        rect = Rectangle(1, 2, 4, 6)
        self.assertEqual(rect.area(), 12)

    def test_move(self):
        rect = Rectangle(1, 2, 3, 4)
        rect.move(1, 1)
        self.assertEqual(rect, Rectangle(2, 3, 4, 5))

    def test_intersection(self):
        rect1 = Rectangle(1, 1, 3, 3)
        rect2 = Rectangle(2, 2, 4, 4)
        rect3 = Rectangle(4, 4, 5, 5)
        self.assertEqual(rect1.intersection(rect2), Rectangle(2, 2, 3, 3))
        self.assertIsNone(rect1.intersection(rect3))

    def test_cover(self):
        rect1 = Rectangle(1, 1, 3, 3)
        rect2 = Rectangle(2, 2, 4, 4)
        rect3 = Rectangle(4, 4, 5, 5)
        self.assertEqual(rect1.cover(rect2), Rectangle(1, 1, 4, 4))
        self.assertEqual(rect1.cover(rect3), Rectangle(1, 1, 5, 5))

    def test_make4(self):
        rect = Rectangle(1, 1, 3, 3)
        rects = rect.make4()
        self.assertEqual(rects[0], Rectangle(1, 1, 2, 2))
        self.assertEqual(rects[1], Rectangle(2, 1, 3, 2))
        self.assertEqual(rects[2], Rectangle(1, 2, 2, 3))
        self.assertEqual(rects[3], Rectangle(2, 2, 3, 3))

if __name__ == "__main__":
    unittest.main()
