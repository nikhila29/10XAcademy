n = int(input())
for i in range(n):
	x = int(input())
	f = 0
	for j in range(2, x): 
		if(x%j == 0): 
			f = 1
			break
	if(f == 0):
		print("Yes")
	else:
		print("No")