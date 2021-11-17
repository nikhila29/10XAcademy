#area--length*width,  perimeter----2(length*width)
class Rectangle:
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def rectangle_area(self):
        if self.l>0 and self.w>0:
            area=self.l*self.w
            return area
        else:
            return 0
    def rectangle_perimeter(self):
        if self.l>0 and self.w>0:
            perimeter=2*(self.l+self.w)
            return perimeter
        else:
            return 0


if __name__ == "__main__":
    newRectangle = Rectangle(int(input()), int(input()))
    print(newRectangle.rectangle_area())
    print(newRectangle.rectangle_perimeter())