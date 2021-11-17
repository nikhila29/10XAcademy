# your code goes here
def result(i,arr,remaining_sum):
	if (remaining_sum==0 and i==len(arr)):
		return (1)
	if (i==len(arr) and remaining_sum!=0):
		return (0)
	return (result(i+1,arr,remaining_sum-arr[i])+result(i+1,arr,remaining_sum+arr[i])+ result(i+1,arr,remaining_sum))
target=int(input())
N=int(input())
arr=[int(i) for i in input().split()]
print(result(0,arr,target))