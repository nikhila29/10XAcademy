#n=int(input())
#arr=[]
#for i in range(n):
#    arr.append(int(input()))
#res=[]
#for i in range(0,n-2):
#    for j in range(i+1,n-1):
#        for k in range(j+1,n):
#            max_product=(arr[i]*arr[j]*arr[k])
#            res.append(max_product)
#print(max(res))
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
arr.sort()
print(max(arr[-1]*arr[-2]*arr[-3],arr[0]*arr[1]*arr[-1]))