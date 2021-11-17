n,x=map(int,input().split())
numbers=list(map(int,input().split()))
count=0
for i in numbers:
    if i%x==0:
        count+=1
print(count)
