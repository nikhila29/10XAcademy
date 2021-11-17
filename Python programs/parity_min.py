# your code goes here
n=int(input())
arr=[]
for i in range(n):
	arr.append(int(input()))
min_ele=min(arr)
if min_ele<0:
	min_ele*=(-1)
sum_of_digits=sum([int(x) for x in str(min_ele)])
if sum_of_digits%2!=0:
	print(0)
else:
	print(1)