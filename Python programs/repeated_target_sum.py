def targetSum(arr, key):
    count= [1] + [0] * key
    for i in arr:
        for j in range(0, key - i + 1):
            count[j + i] += count[j]
    return count[key]
n,key=map(int,input().split())
arr=[int(x) for x in input().split()]
print(targetSum(arr,key))