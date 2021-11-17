n,k=map(int,input().split())
nums=list(map(int,input().split()))
count=0
for i in nums:
    if i==k:
        count+=1
print(count)