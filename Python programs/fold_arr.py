n=int(input())
arr=[]
for _ in range(n):
    arr.append(int(input()))
f=int(input())
while f>0:
    temp=[0]*(len(arr)//2)
    for i in range(len(arr)//2):
        temp[i]=arr[i]+arr[-i-1]
    if (len(arr)%2==1):
        temp.append(arr[len(arr)//2])
    arr=temp
    f-=1
print(len(arr))
for i in arr:
    print(i)