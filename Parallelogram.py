
import math

class Parallelogram:
    def __init__(self,len,width,angle):
        self.len=len
        self.width=width
        self.angle=angle

    def perimeter(self):
        return self.len*2 + self.width*2

    def area(self):
        radian = math.radians(self.angle)
        return self.len * self.width * math.sin(radian)

class Rhombus(Parallelogram):
    def __init__(self, len, angle):
        super().__init__(len, len, angle)

class Square(Rhombus):
    def __init__(self,len):
        super().__init__(len, 90)

if __name__ == '__main__':

    paral = Parallelogram(5,6,60)
    print(paral.area())
    print(paral.perimeter())

    rh = Rhombus(5,60)
    print(rh.perimeter())
    print(rh.area())

    sq = Square(5)
    print(sq.perimeter())
    print(sq.area())
