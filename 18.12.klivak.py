class CompareMixin:
    def __eq__(self, other):
        return not self < other and not other < self

    def __ne__(self, other):
        return self < other or other < self

    def __lt__(self, other):
        raise NotImplementedError("__lt__ повинні бути реалізовані в підкласі")

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return other < self

    def __ge__(self, other):
        return other < self or self == other

class Point2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

class XOrderPoint2(Point2, CompareMixin):
    def __lt__(self, other):
        return self.x < other.x

class FullXOrderPoint2(XOrderPoint2):
    pass

class YOrderPoint2(Point2, CompareMixin):
    def __lt__(self, other):
        return self.y < other.y

class FullYOrderPoint2(YOrderPoint2):
    pass

class DistOrderPoint2(Point2, CompareMixin):
    def __lt__(self, other):
        return (self.x**2 + self.y**2) < (other.x**2 + other.y**2)

class FullDistOrderPoint2(DistOrderPoint2):
    pass

points = [XOrderPoint2(2, 3), XOrderPoint2(1, 5), XOrderPoint2(4, 2)]
sorted_points = sorted(points)

for point in sorted_points:
    print(point)
