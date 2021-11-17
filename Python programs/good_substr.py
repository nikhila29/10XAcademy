n,q=map(int,input().split())
str=input()
res=[]
count=0
for i in range(len(str)):
    if str[i]=='1':
        count+=1
    res.append(count)
for i in range(q):
    l,r=map(int,input().split())
    ones=(res[r-1]-res[l-2] if l>1 else res[r-1])
    zero=(r-l+1)-ones
    if ones==zero:
        print('yes')
    else:
        print('no')