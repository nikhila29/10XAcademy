# your code goes here
def recursiveMultiply(n):
	if n<10:
		return n
	return (n%10)*(recursiveMultiply(n//10))

for _ in range(int(input())):
	n=int(input())
	if n<0:
		n*=(-1)
	print(recursiveMultiply(n))