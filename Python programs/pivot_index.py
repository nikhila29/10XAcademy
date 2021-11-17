def pivotIndex(arr):
	left_sum=0
	right_sum=sum(arr[1:])
	
	for i in range(len(arr)-1):
		if left_sum==right_sum:
			return i
		left_sum+=arr[i]
		right_sum-=arr[i+1]
		
	if left_sum==right_sum:
		return len(arr)-1
	return -1


# Do not edit anything below
if __name__ == "__main__":
    num_elems = int(input())
    nums = []
    for i in range(num_elems):
        nums.append(int(input()))
        
    print(pivotIndex(nums))