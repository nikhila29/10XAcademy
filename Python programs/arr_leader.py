# your code goes here
def leader(a,n):
	res=[]
	maxx=float('-inf')
	for i in range(n-1,-1,-1):
		maxx=max(maxx,a[i])
		if a[i]==maxx:
			res.append(a[i])
	return res
n=int(input())
arr=[]
for i in range(n):
	arr.append(int(input()))
for i in leader(arr,n):
	print(i)