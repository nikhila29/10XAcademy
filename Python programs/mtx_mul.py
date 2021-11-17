# your code goes here
n1=int(input())
arr1=[[int(x) for x in input().split()] for j in range (n1)]

n2=int(input())
arr2=[[int(x) for x in input().split()] for j in range (n2)]

result=[]

for i in range(n1):
	temp=[]
	for j in range(len(arr2[0])):
		summ=0
		for k in range(n2):
			summ+=arr1[i][k]*arr2[k][j]
		temp.append(summ)
	result.append(temp)
	
print(len(result))
for i in result:
	print(*i)

		
