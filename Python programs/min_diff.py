n=int(input())
arr=list(map(int,input().split()))
arr.sort()
diff=[]
for i in range(1,n):
    sub=arr[i]-arr[i-1]
    diff.append(sub)
print(min(diff))
    
        
        