#n,q=5,3
                    #  0,1,2,3,4
#n=5--> initially arr =[0,0,0,0,0]
#1st--> 0,3,4(l,r,val) -->arr=[4,4,4,4,0]
#2nd-->3,4,1(l,r,val)-->arr=[4,4,4,4+1,1]
#3rd-->1,3,5(l,r,val)-->arr=[4,4+5,4+5,5+5,1]-->[4,9,9,10,1]
n,q=map(int,input().split())
arr=[0]*n #[0,0,0,0,0]
for _ in range(q):# upto 3
    l,r,val=map(int,input().split())
    arr[l]+=val 
    if r<n-1: # if r=3 3<4
        arr[r+1]-=val #arr[4]
for i in range(1,n):# 1 to 5
    arr[i]+=arr[i-1] 
print(*arr)


