# your code goes here
n=int(input())
string=input()
x=list(map(str,input().split()))
ind=True
for i in string:
    if i not in x:
    	ind=False
if ind==True:
	print('true')
else:
	print('false')