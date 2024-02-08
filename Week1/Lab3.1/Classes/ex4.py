import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"Координаты точки: ({self.x}, {self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        distance = math.sqrt(dx**2 + dy**2)
        return distance

point1 = Point(3, 4) # изначальные точки
point2 = Point(6, 8)

point1.show()

# Изменение координат второй точки
point2.move(2, -1)

point2.show()

# расстояние между точками
distance = point1.dist(point2)
print(f"Расстояние между точками: {distance}")
