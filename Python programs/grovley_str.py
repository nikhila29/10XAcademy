# your code goes here
# abcde
# Y= 2*97+1*98+0*99+1*100+2*101
#result=bdeca
#res2=acedb

#abc  Y=1*97+0*98+1*99=196
#bca----Y=1*98+0*99+1*97=195
#cab----Y=1*99+0*97+1*98=197

#abcxy=acyxb
#acy xb
n=int(input())
for _ in range(n):
	s=input()
	s=list(s)
	s=sorted(s)
	res=''
	for i in range(0,len(s),2):
		res+=s[i]
	for i in range(len(s)-2,0,-2):
		res+=s[i]
	print(res)
	

	


