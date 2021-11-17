#17 28 30
#99 16 8
#a[i] >b[i]--->alice-->1-->28>16,30>8--2
#a[i]<b[i]---->bob-->1---->17<99,--1
#a[i]==b[i]--->neither person receives a point

a=list(map(int,input().split()))
b=list(map(int,input().split()))
alice=0
bob=0
for i in range(3):
    if a[i]>b[i]:
        alice+=1
    elif(a[i]<b[i]):
        bob+=1
res=[alice,bob]
print(*res)

