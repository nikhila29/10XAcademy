#area--pi*r**2,circumference----2*pi*r
class Circle:
    def __init__(self,r):
        self.r=r
    def getArea(self):
        pi=3.14
        if self.r>0:
            area=pi*self.r*self.r
            return area
        else:
            return 0
    def getCircumference(self):
        pi=3.14
        if self.r>0:
            circumference=2*pi*self.r
            return circumference
        else:
            return 0


if __name__ == "__main__":
    one_circle = Circle(float(input()))
    print(float(one_circle.getArea()))
    print(float(one_circle.getCircumference()))