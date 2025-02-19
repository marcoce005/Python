import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x, self.__y = x, y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.sqrt(abs(self.__x - x) ** 2 + abs(self.__y - y) ** 2)

    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertices = [vertice1, vertice2, vertice3]

    def perimeter(self):
        return sum(
            [
                e.distance_from_point(el)
                for i, e in enumerate(self.__vertices)
                for el in self.__vertices[i + 1 :]
            ]
        )


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
