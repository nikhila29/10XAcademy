def peak(arr,n):
    for i in range(n):
        if((i==0 or arr[i]>arr[i-1]) and (i==(n-1) or arr[i]>arr[i+1])):
            return i+1
    return -1
testcases=int(input())
for i in range(testcases):
    size=int(input())
    arr=[int(x) for x in input().split()]
    print(peak(arr,size))