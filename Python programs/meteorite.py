# your code goes here
def distinct(arr):
	count=1
	for i in range(1,len(arr)):
		if(arr[i]!=arr[i-1]):
			count+=1
	return(count)
def min_cons(arr):
	minm=999999
	for i in range(1,len(arr)):
		if(arr[i]!=arr[i-1]):
			minm=min(minm,arr[i]-arr[i-1])
	return(minm)
def max_cons(arr):
	maxm=-999999
	for i in range(1,len(arr)):
		maxm=max(maxm,arr[i]-arr[i-1])
	return(maxm)
T=int(input())
for j in range(T):
	M,N,Q=[int(i) for i in input().split()]
	X=[1,M]
	Y=[1,N]
	for _ in range(Q):
		x,y=[int(i) for i in input().split()]
		X.append(x)
		Y.append(y)
	X.sort()
	Y.sort()
	print((distinct(X)-1)*(distinct(Y)-1),min_cons(X)*min_cons(Y),max_cons(X)*max_cons(Y))
