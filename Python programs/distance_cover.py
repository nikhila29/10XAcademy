#0,1,2,3,4,5,6,7===0,1,2,3,5,8,13,21
def distance(arr):
    if arr<0:
        return 0
    if arr==0:
        return 1
    return distance(arr-1)+distance(arr-2)

n=int(input())
for _ in range(n):
    arr=int(input())
    print(distance(arr))