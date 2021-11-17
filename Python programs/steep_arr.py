n=int(input())
arr=list(map(int,input().split()))
arr1=[]
for i in range(n):
    maxm=max(arr[i+1:])
    sub=maxm-arr[i]
    arr1.append(sub)
sum=0
for i in arr1:
    sum+=i
print(sum)
