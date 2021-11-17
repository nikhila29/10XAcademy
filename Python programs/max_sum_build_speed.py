def maxSumBuild(arr):
    arr.sort()
    res=0
    for i in range(0,2*n,2):
        res+=arr[i]
    return (res)
n=int(input())
arr=[int(x) for x in input().split()]
print(maxSumBuild(arr))