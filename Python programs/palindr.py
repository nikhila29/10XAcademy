s=input()
n=int(input())
pal=s[::-1]
if len(s)==1:
    print(s)
elif n==0:
	print(s+pal)
else:	
    print(s+pal[1:])
