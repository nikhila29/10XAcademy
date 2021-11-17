def insertTarget(arr,n,x):
    if x<=arr[0]:
        return [x]+arr
    if x>=arr[-1]:
        return arr+[x]
    for i in range(1,n):
        if x<=arr[i]:
            return arr[:i] + [x] + arr[i:]

for _ in range(int(input())):
    n,x=map(int,input().split())
    arr=list(map(int,input().split()))
    print(*insertTarget(arr,n,x))
