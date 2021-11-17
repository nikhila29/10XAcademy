# your code goes here
def summation(n):
	res = 0
	while(n):
		res += n//5
		n = n//5
	return res
	
t = int(input())
for  test in range(t):
	n = int(input())
	low = 1
	high = 10**18
	ans = -1
	while(low<=high):
		mid = (low+high)//2
		if(summation(mid)>=n):
			ans = mid
			high = mid-1
		else:
			low = mid+1
	print(ans-ans%5)
