def perimeter(l,b):
    if l>0 and b>0:
        p=2*(l+b)
        return (p)
    else:
        return (0)
l=int(input())
b=int(input())
print(perimeter(l,b))