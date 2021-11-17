n=int(input())
arr=[int(i) for i in input().split()]
arr.sort()
res=[arr[0]]
for i in arr:
    if(res[-1]!=i):
        res.append(i)
for i in range(len(res)-2):
    print(res[i],end=" ")
if len(res)<=2:
    print(-1)