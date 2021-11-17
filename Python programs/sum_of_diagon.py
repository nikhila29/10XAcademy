# your code goes here
n=int(input())
arr=[[int(x) for x in input().split()] for j in range(n)]
sum1,sum2=0,0
for i in range(n):
	for j in range(n):
		if i==j:
			sum1+=arr[i][j]
		if i+j==n-1:
			sum2+=arr[i][j]
print(sum1+sum2)