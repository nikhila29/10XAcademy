c=1000000007
t=int(input())
for _ in range(t):
    n=int(input())
    arr=[int(i) for i in input().split()]
    arr.sort()
    SUM=sum(arr)
    sumi=0
    total=0
    for i in range(len(arr)):
        sumi=(sumi%c+arr[i]%c)%c 
        rem=(SUM%c - sumi%c)%c 
        total=(total%c+(rem%c -(arr[i]%c*(len(arr)-i-1)%c)%c)%c)%c 
    print((total%c*max(arr)%c)%c)