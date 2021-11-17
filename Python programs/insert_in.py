n,x=[int(i) for i in input().split()]
arr=list(map(int,input().split()))
arr.append(x)
j=len(arr)-2
temp=arr[-1]
while j>=0 and x<arr[j]:
    arr[j+1]=arr[j]
    j-=1
arr[j+1]=x
for i in arr:
    print(i,end=" ")