def shuffle(arr):
	pos=1
	mid=len(arr)//2
	for d in range(mid,len(arr)):
		j=d
		while j>pos:
			arr[j],arr[j-1]=arr[j-1],arr[j]
			j-=1
		pos+=2
	return arr

# Do not edit anything below
if __name__ == "__main__":
    n = int(input())
    nums = []
    for index in range(2 * n):
        nums.append(int(input()))
    for elem in shuffle(nums):
        print(elem)