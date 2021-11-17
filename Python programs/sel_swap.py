def selectSwap(arr, n):
	maxi=float('-inf')
	maxi_ind=-1
	mini=float('inf')
	mini_ind=-1
	for i in range(n):
		if arr[i]>maxi:
			maxi=arr[i]
			maxi_ind=i
		if arr[i]<mini:
			mini=arr[i]
			mini_ind=i
	arr[maxi_ind],arr[mini_ind]=arr[mini_ind],arr[maxi_ind]
	return arr
	


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        print(*selectSwap(arr, n))