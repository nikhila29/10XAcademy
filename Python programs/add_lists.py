t=int(input())
while t>0:
	a=[int(i) for i in input().split()]
	b=[int(i) for i in input().split()]
	while (len(a)<len(b)):
		a+=[0]
	while (len(a)>len(b)):
		b+=[0]
	carry=0
	result=""
	for i in range(len(a)):
		add=a[i]+b[i]+carry
		result+=str(add%10)
		carry=add//10
	if carry==1:
		result+=str(1)
	print(result)
	t-=1