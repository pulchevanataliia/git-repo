# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:

    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    @property
    def length(self):
        return ((self.p2.x - self.p1.x) ** 2 + (self.p2.y - self.p1.y) ** 2) ** 0.5

    @property
    def k(self):
        return (self.p2.y - self.p1.y) / (self.p2.x - self.p1.x) if self.p2.x - self.p1.x != 0 else float("inf")

class Triangle:

    def __init__(self, *args):
        self.p1 = args[0]
        self.p2 = args[1]
        self.p3 = args[2]
        self.a = Line(self.p1, self.p2)
        self.b = Line(self.p2, self.p3)
        self.c = Line(self.p3, self.p1)

    def area(self):
        p = self.perimeter() / 2
        return (p * (p - self.a.length) * (p - self.b.length) * (p - self.c.length))**0.5

    def perimeter(self):
        return self.a.length + self.b.length + self.c.length

    def hight(self):
        h1 = 2 * self.area() / self.a.length
        h2 = 2 * self.area() / self.b.length
        h3 = 2 * self.area() / self.c.length
        return min(h1, h2, h3)

triangle = Triangle(Point(0, 0), Point(4, 0), Point(2, 4))
print(f"Площадь треугольника = {triangle.area():.3f}")
print(f"Периметр треугольника = {triangle.perimeter():.3f}")
print(f"Высота треугольника = {triangle.hight():.3f}")
print()
