n,q=map(int,input().split())
arr=list(map(int,input().split()))
for i in range(1,n):
    arr[i]=arr[i]+arr[i-1]
for i in range(q):
    l,r=map(int,input().split())
    if l == 1:
        print(arr[r-1])
    else:
        print(arr[r-1] - arr[l-1-1])