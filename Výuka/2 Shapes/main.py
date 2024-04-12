import math


class Shape:
    def __init__(self):
        print("Vykresluji tvar: ")


class Square(Shape):
    def __init__(self, a):
        super().__init__()
        self.a = a

    def perimeter(self):
        return 2 * self.a

    def area(self):
        return self.a * self.a

    def print(self):
        print("Strana: ", self.a)


class Rectangle(Square):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b

    def print(self):
        print("Strana a: ", self.a, " Strana b: ", self.b)


class Cube(Square):
    def __init__(self, a):
        super().__init__(a)

    def volume(self):
        return self.a * self.a * self.a

    def print(self):
        print("Strana: ", self.a)


class Block(Rectangle):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def volume(self):
        return self.a * self.b * self.c

    def print(self):
        print("Strana a: ", self.a, "Strana b: ", self.b, "Strana c: ", self.c)


class Circle(Shape):
    def __init__(self, r):
        super().__init__()
        self.r = r

    def perimeter(self):
        return 2 * math.pi * self.r

    def area(self):
        return math.pi * self.r * self.r

    def print(self):
        print("Polomer r: ", self.r)


class Sphere(Circle):
    def __init__(self, r):
        super().__init__(r)

    def surface(self):
        return 4 * math.pi * self.r * self.r

    def volume(self):
        return 4 / 3 * math.pi * pow(self.r, 3)

    def print(self):
        print("Polomer r: ", self.r)


class Cylinder(Circle):
    def __init__(self, r, v):
        super().__init__(r)
        self.v = v

    def surface(self):
        return 2 * self.area() + 2 * self.perimeter() * self.v

    def volume(self):
        return self.area() * self.v

    def print(self):
        print("Polomer r: ", self.r, "Vyska v: ", self.v)


square = Square(2)
square.print()
print("Obsah ctverce: ", square.area(), "\n")

cube = Cube(3)
cube.print()
print("Objem krychle: ", cube.area(), "\n")

block = Block(3, 5, 2)
block.print()
print("Objem kvadru: ", block.volume(), "\n")


circle = Circle(4)
circle.print()
print("Obvod kruhu: ", circle.perimeter(), "\n", "Obsah kruhu: ", circle.area(), "\n")

sphere = Sphere(5)
sphere.print()
print("Povrch koule: ", sphere.surface(), "\n", "Objem koule: ", sphere.volume(), "\n")

cylinder = Cylinder(3, 4)
cylinder.print()
print("Povrch valce: ", cylinder.surface(), "\n", "Objem valce: ", cylinder.volume(), "\n")
