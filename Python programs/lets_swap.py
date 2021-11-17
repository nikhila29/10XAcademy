n=int(input())
arr=list(map(int,input().split()))
maxm=[]
minim=[]
res=0
for i in range(1,n+1):#1,2,3,4,5  
    res+=abs(arr[i-1]-i) 
    maxm.append(max(arr[i-1],i))
    minim.append(min(arr[i-1],i))
res+=2*(max(minim)-min(maxm))
print(res)