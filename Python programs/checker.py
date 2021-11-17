t=int(input())
for _ in range(t):
    arr=list(map(int,input().split()))
    n=int(input())
    search_ele=list(map(int,input().split()))
    for i in search_ele:
        if i in arr:
            print(i)
        else:
            print(-1)
