# your code goes here
n=int(input())
arr=[]
for i in range(n):
	arr.append(int(input()))
if len(arr)==0:
	print(-1)
else:
	count=1
	maxm=1
	for i in range(len(arr)-1):
		if arr[i]==arr[i+1]:
			count+=1
			maxm=max(maxm,count)
			continue
		count=1
	res=[-1]
	for i in arr:
		if (arr.count(i)==maxm and res[-1]!=i):
			res.append(i)
	for i in res[1:]:
		print(i)