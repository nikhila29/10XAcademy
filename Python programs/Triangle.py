import math
def Triangle(b,a):
    return math.ceil((2*a)/b)
n=int(input())
for _ in range(n):
    b,a=map(int,input().split())
    print(Triangle(b,a))