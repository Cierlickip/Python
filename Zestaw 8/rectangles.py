# 8.1

from points import Point

class Rectangle:

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

    @property
    def center(self):
        delta_x = self.pt2.x - self.pt1.x
        center_x = delta_x / 2
        delta_y = self.pt2.y - self.pt1.y
        center_y = delta_y / 2

        return Point(center_x + self.pt1.x, center_y + self.pt1.y)

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


    def from_points(cls, points):
        if isinstance(points, (list, tuple)):
            if len(points) != 2:
                raise ValueError("Arguments must be 2 lists/tuples")
            point1 = points[0]
            point2 = points[1]

        if not isinstance(point1, Point) or not isinstance(point2, Point):
            raise ValueError("Arguments must be points!")

        return cls(point1.x, point1.y, point2.x, point2.y)

    @property
    def top(self):
        return self.pt2.y

    @property
    def bottom(self):
        return self.pt1.y

    @property
    def left(self):
        return self.pt1.x

    @property
    def right(self):
        return self.pt2.x

    @property
    def width(self):
        return abs(self.pt2.x - self.pt1.x)

    @property
    def height(self):
        return abs(self.pt2.y - self.pt1.y)

    @property
    def topleft(self):
        return Point(self.pt1.x, self.pt2.y)

    @property
    def topright(self):
        return Point(self.pt2.x, self.pt2.y)

    @property
    def bottomleft(self):
        return Point(self.pt1.x, self.pt1.y)

    @property
    def bottomright(self):
        return Point(self.pt2.x, self.pt1.y)
