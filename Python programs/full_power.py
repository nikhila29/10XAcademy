testno=int(input())
for i in range(testno):
    no=int(input())
    arr=list(map(int,input().strip().split()))
    minn=min(arr)
    maxx=max(arr)
    if no>2 and maxx==arr[0] and minn==arr[-1]:
        print(max(maxx-min(arr[1:-1]),max(arr[1:-1])-minn))
    else:
        print(maxx-minn)