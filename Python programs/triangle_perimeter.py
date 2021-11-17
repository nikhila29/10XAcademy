def perimeter(arr):
    arr.sort()
    for i in range(len(arr)-3,-1,-1):
        if arr[i]+arr[i+1] > arr[i+2]:
            return (arr[i]+arr[i+1]+arr[i+2])
    return 0
for i in range(int(input())):
    arr=[int(x) for x in input().split()]
    print(perimeter(arr))