m=int(input())
n=int(input())
i=m
count=0
while i<=n:
    if i>=0:
        print(i)
        count+=1
    i+=1
if count==0:
    print(-1)