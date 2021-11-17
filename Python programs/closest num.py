# your code goes here
# your code goes here
def insert(arr,K):
	l=0
	r=len(arr)-1
	if K>arr[-1]:
		return(len(arr))
	if(K<arr[0]):
		return(0)
	while(l<=r):
		mid=(l+r)//2
		if(arr[mid]==K):
			return(mid)
		if(arr[mid]<K and arr[mid+1]>K):
			return(mid+1)
		if(arr[mid]>K and arr[mid-1]<K):
			return(mid)
		if(arr[mid]>K):
			r=mid-1
		else:
			l=mid+1
	return(mid)
	
N,Q=[int(i) for i in input().split()]
arr=[int(i) for i in input().split()]
queries=[int(i) for i in input().split()]
for q in queries:
	index=insert(arr,q)
	if index==0:
		print(arr[0],end=" ")
	elif index==len(arr):
		print(arr[-1],end=" ")
	else:
		if(arr[index]-q>q-arr[index-1]):
			print(arr[index-1])
		else:
			print(arr[index])
