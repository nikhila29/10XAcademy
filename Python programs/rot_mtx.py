# your code goes here
def rotateMatrix(matrix,rows):
	
	rotated=[]
	cols=len(matrix[0])
	
	for j in range(cols):
		temp=[]
		for i in range(rows):
			temp.append(matrix[i][j])
		rotated.append(temp[::-1])
	return rotated
	
n=int(input())
arr=[[int(x) for x in input().split()] for j in range(n)]
result=rotateMatrix(arr,n)
print(len(result))
for i in result:
	print(*i)