# your code goes here
def increasingSubarray(a,n):
	length=1
	count=1
	end=1
	for i in range(1,n):
		if a[i]>a[i-1]:
			count+=i
		else:
			if count>length:
				length=count
				end=i
			count=1
	if count>=length:
		length=count
		end=n
	return [length,end-length+1,end]
n=int(input())
arr=[int(x) for x in input().split()]
print(*increasingSubarray(arr,n))