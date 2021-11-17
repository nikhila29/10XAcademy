n=int(input())
arr=[]
index=[]
for i in range(n):
    arr.append(int(input()))
for i in range(n):
    index.append(int(input()))
target=[]
for i in range(n):
    target.append(arr[i])
    temp=arr[i]
    j=i-1
    while j>=index[i]:
        target[j+1]=target[j]
        j-=1
    target[j+1]=temp
for i in target:
    print(i)

