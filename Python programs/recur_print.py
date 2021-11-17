# your code goes here
T=int(input())
def display(l,r):
	if (l>r):
		return
	print(l)
	display(l+1,r)
for _ in range(T):
	l,r=[int(i) for i in input().split()]
	display(l,r)