# your code goes here
def numberOfOnes(num):
	return bin(num).count('1')

n=int(input())
res=[]

for i in range(12):
	for j in range(60):
		if (numberOfOnes(i)+numberOfOnes(j)==n):
			time="%02i:%02i" %(i,j)
			res.append(str(time))
res=sorted(res)
if len(res)==0:
	print(-1)
else:
	print(*res)