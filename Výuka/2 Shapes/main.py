class Shape:
    def __init__(self):
        print("Vykresluji tvar: ")


class Square(Shape):
    def __init__(self, a):
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
        print("Strana a: ", self.a, " Strana b: ", self.b, " Strana c: ", self.c)


square = Square(2)
square.print()
print("Obsah ctverce: ", square.area(), "\n")

cube = Cube(3)
cube.print()
print("Objem krychle: ", cube.area(), "\n")

block = Block(3, 5 ,2)
block.print()
print("Objem kvadru: ", block.volume(), "\n")