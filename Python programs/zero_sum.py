def zeroSum(matrix, rows, cols):
    count=0
    for i in range(rows):
        sum=0
        for j in range(cols):
            sum+=matrix[i][j]
        if sum==0:
            count+=1
    for j in range(cols):
        sum=0
        for i in range(rows):
            sum+=matrix[i][j]
        if sum==0:
            count+=1
    return count


for _ in range(int(input())):
    n,m = map(int, input().split())
    arr = [[int(x) for x in input().split()] for i in range(n)]
    print(zeroSum(arr, n, m))