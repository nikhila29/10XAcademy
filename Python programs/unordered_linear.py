
#k=int(input())
#n=int(input())
#a=[]
#for i in range(n):
#    a.append(int(input()))
#for index,val in enumerate(a):
 #   if k==val:
  #      print(index)
   # print(-1)
# your code goes here
k=int(input())
n=int(input())
index=0
ind=0
for j in range(n):
	if (k==int(input())):
		print(index)
		ind=1
		break
	index+=1
if ind==0:
	print(-1)
