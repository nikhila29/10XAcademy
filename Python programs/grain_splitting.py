#2 1 1 4 3 3
#1 1 2 3 3 4
#1 1 2 3 3    4----1+1+2+3+3(10)=4
#1 1 2 3     3 4-----1+1+2+3(7)==3+4
def grains(arr):
    n=len(arr)
    arr.sort()
    sum1=sum(arr)
    left_sum=sum1  # 2+1+1+4+3+3=14
    right_sum=0
    right=[]
    for i in range(n-1,-1,-1): # 0,-1,-1
        right_sum+=arr[i] 
        left_sum-=arr[i]
        right.append(arr[i])
        if left_sum==right_sum:
            return right[::-1]
n=int(input())
print(n)
for i in range(n):
    arr=list(map(int,input().split()))
    print(*grains(arr))