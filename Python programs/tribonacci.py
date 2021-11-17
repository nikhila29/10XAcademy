trib=[0,0,1]
n=int(input())
for i in range(3,n):
	trib.append(trib[i-1]+trib[i-2]+trib[i-3])
print(trib[-1])