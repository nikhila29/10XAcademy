n=int(input())
arr=list(map(int,input().split()))
arr.sort
res=[]
for i in arr:
    if i!=i+1:
        res.append(i)
    print(*res)
    
