class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def calculatePerimeter(self):
        perimeter=2*(self.length+self.breadth)
        return perimeter 
### DO NOT CHANGE ANYTHING BELOW THIS LINE

if __name__ == '__main__':
    
    l, w = map(int, input().split())
    r1 = Rectangle(l, w)
    print(r1.calculatePerimeter())