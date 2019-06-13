#1

class Apple:
    def __init__(self, w, c, f, s):
        self.weight = w
        self.color = c
        self.fragrance = f
        self.size = s
        print("Created!")

ap1 = Apple(100, "red", "sweet", 8)
print(ap1.fragrance)


#2

import math

class Circle:
    def __init__(self, d):
        self.diameter = d

    def area(self):        
        return (((self.diameter/2) ** 2) * math.pi)

circle = Circle(8)
print(circle.area())


#3

class Triangle:
    def __init__(self, b, h):
        self.base = b
        self.height = h

    def area(self):
        return (self.base * self.height) / 2

triangle = Triangle(20, 30)
print(triangle.area())


#4

class Hexagon:
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3
        self.side4 = s4
        self.side5 = s5
        self.side6 = s6

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3 + self.side4 + self.side5 + self.side6

hexagon = Hexagon(1, 2, 3, 4, 5, 6)
print(hexagon.calculate_perimeter())
        
