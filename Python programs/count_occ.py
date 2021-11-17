n=int(input())
list=[]
for i in range(0,n):
    nums=int(input())
    list.append(nums)
q=int(input())
count=0
for j in list:
    if q==j:
        count+=1
print(count)
