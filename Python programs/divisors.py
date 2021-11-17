
def sumofdivisors(n):
	i=1
	sum=0
	while i<=n:
		if n%i==0:
			sum+=i
		i+=1
	return (sum)
    
n = int(input())
print(sumofdivisors(n))
        