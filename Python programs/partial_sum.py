n,x=map(int,input().split())
list=[int(i) for i in input().split()]
sum=0
for i in list:
    sum+=i 
ind=0
for i in list:
    if (sum-i)==x:
        ind=1
        break
if ind==0:
    print(0)
else:
    print(1)