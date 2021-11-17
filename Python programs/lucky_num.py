def findLuckyNumber(nums):
	count=1
	for i in range(1,len(nums)):
		if nums[i]==nums[i-1]:
			count+=1
		else:
			if count==nums[i-1]:
				return nums[i-1]
			count=1
	if count==nums[-1]:
		return nums[-1]
	return -1
		

# DO NOT change anything below this line
if __name__ == "__main__":
    num_elems = int(input())
    input_arr = []
    for index in range(num_elems):
        input_arr.append(int(input()))
    
    print(findLuckyNumber(input_arr))