list=[]
n=int(input())
sum=0
for i in range(0,n):
    nums=int(input())
    list.append(nums)
    sum=sum+list[i]
avg=sum//n
print(sum)
print(avg)    
    