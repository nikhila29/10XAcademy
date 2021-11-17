# your code goes here
T=int(input())
def have_sol(N):
	if N==1:
		return (True)
	if (N<1):
		return (False)
	div_10=False
	div_20=False
	if (N%10==0):
		div_10=have_sol(N//10)
	if (N%20==0):
		div_20=have_sol(N//20)
	return (div_10 or div_20)
for _ in range(T):
	N=int(input())
	if (have_sol(N)):
		print("Yes")
	else:
		print("No")