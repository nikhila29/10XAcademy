n=int(input())
pos=[0]*n 
for i in range(n):
    p,v=map(int,input().split())
    pos[p]=v
count=[0]*11
res=0
for i in range(n):
    for j in range(pos[i]+1,11):
        res+=count[j]
    count[pos[i]]+=1
print(res)