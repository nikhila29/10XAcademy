n=int(input())
for _ in range(n):
    arr=[int(i) for i in input().split()]
    even=arr[0::2]
    odd=arr[1::2]
    even.sort()
    odd.sort()
    even=even[::-1]
    e=0
    for i in even:
        arr[e]=i 
        e+=2
    o=1
    for i in odd:
        arr[o]=i 
        o+=2
    print(*arr)