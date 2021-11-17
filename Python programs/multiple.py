def multiple(n):
    if n%2!=0:
        mul=(2*n)
        return mul
    if n%2==0:
        lcm=(2*n)//2
        return lcm

n=int(input())
print(multiple(n))
