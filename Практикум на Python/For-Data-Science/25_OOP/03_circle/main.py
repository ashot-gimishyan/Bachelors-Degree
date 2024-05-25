

from math import pi, sqrt
class Circle:

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def area(self):
        return pi * self.r * self.r

    def perim(self):
        return 2 * pi * self.r

    def change_size(self, k):
        self.r *= k

    def intersect(self, Other):
        centers_dist = sqrt((Other.x - self.x)**2 + (Other.y - self.y)**2)
        if centers_dist <= self.r + Other.r:
            return True
        return False



circle_0_0 = Circle(0, 0, 1)

print(circle_0_0.area())
print(circle_0_0.perim())

circle_0_0.change_size(10)

print(circle_0_0.area())
print(circle_0_0.perim())


circle_2_0 = Circle(2, 0, 2)

print(circle_0_0.intersect(circle_0_0))

circle_2_10 = Circle(10, 10, 1)

print(circle_0_0.intersect(circle_2_10))
