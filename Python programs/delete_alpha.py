n,k=map(int,input().split())
arr=[]
for i in range(n):
    arr.append(input())
deleteColumns=0
for j in range(k):
    col=[]
    for i in range(n):
        col.append(arr[i][j])
    if col!=sorted(col):
        deleteColumns+=1
print(deleteColumns)