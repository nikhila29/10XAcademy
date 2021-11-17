m=int(input())
n=int(input())
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
max_a=0
max_b=0
for i in a:
    max_a=max(max_a,max(i,-i))
for i in b:
    max_b=max(max_b,max(i,-i))
print(max_a*max_b)

