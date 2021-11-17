def rightmost(arr,K):
	l=0
	r=len(arr)-1
	ans=-1
	while(l<=r):
		mid=(l+r)//2
		if(arr[mid]<K):
			l=mid+1
		elif(arr[mid]>K):
			r=mid-1
		else:
			ans=mid
			l=mid+1
            
		mid=(l+r)//2
		if(arr[mid]<K):
			l=mid+1
		elif(arr[mid]>K):
			r=mid-1
		else:
			ans=mid
			r=mid-1
	return(ans)
