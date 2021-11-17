def sumofproduct(n):
    sum=0
    for x in range(1,n+1):
        y=(n//x)
        product=x*y
        sum+=product
    return sum

n = int(input())
print(sumofproduct(n))