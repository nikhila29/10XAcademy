n=int(input())
list=[]
for j in range(0,n):
    nums=int(input())
    list.append(nums)
even_count=0
odd_count=0
for i in list:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print(odd_count)
print(even_count)