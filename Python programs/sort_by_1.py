'''n=int(input())
arr=[int(x) for x in input().split()]
arr.sort()
#x=lambda a:a+10
#print(x(5))
arr.sort(key=lambda x:-bin(x).count("1"))
print(*arr)'''
def count_1(N):
	count=0
	while(N!=0):
		if(N%2==1):
			count+=1
		N//=2
	return(count)
#3
def merge(arr,lmin,lmax,rmin,rmax):
	temp=[]
	l=lmin
	r=rmin
	while(l<=lmax and r<=rmax):
		if(arr[l][0]>=arr[r][0]):
			temp.append(arr[l])
			l+=1
		else:
			temp.append(arr[r])
			r+=1
	while(l<=lmax):
		temp.append(arr[l])
		l+=1
	while(r<=rmax):
		temp.append(arr[r])
		r+=1
	for i in range(lmin,rmax+1):
		arr[i]=temp[i-lmin]
def mergesort(arr,l,r):
	if(l<r):
		mid=(l+r)//2
		mergesort(arr,l,mid)
		mergesort(arr,mid+1,r)
		merge(arr,l,mid,mid+1,r)
N=int(input())
arr=[int(i) for i in input().split()]
#arr=[1,2,3,4,5,6]
#arr=[(num(1),1),(num(2),2).....]
arr=[(count_1(i),i) for i in arr]
mergesort(arr,0,len(arr)-1)
for i in arr:
	print(i[1],end=" ")

