
k=int(input())
n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
for index,val in enumerate(a):
    if k==val:
        print(index)
    print(-1)
    
