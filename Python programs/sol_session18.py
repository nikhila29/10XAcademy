# your code goes here
def max_len_seq(arr):
	Map={}
	maximum=0
	for i in arr:
		if i-1 not in Map:
			Map[i]=1
		else:
			Map[i]=Map[i-1]+1
		maximum=max(maximum,Map[i])
	return(maximum)
		
N=int(input())
arr=[int(i) for i in input().split()]
print(max_len_seq(arr))
# your code goes here
'''N=int(input())
arr=[int(i) for i in input().split()]
arr=[abs(i) for i in arr]
arr_sqr=[i*i for i in arr]
print((sum(arr)**2-sum(arr_sqr))//2)
	while(l<=r):
		mid=(l+r)//2
		if(mid<len(arr)-1 and arr[mid]>arr[mid+1]):
			return(arr[mid+1])
		elif(mid>0 and arr[mid]<arr[mid-1]):
			return(arr[mid])
		elif(arr[mid]>arr[l]):
			l=mid+1
		else:
			r=mid-1
	return(arr[-1])
	
N=int(input())
arr=[int(i) for i in input().split()]
print(minimum(arr))'''
