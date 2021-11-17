n=int(input())
a=list(map(int,input().split()))
maxm=a[0]
for i in a:
    if i>maxm:
        maxm=i 

minim=a[0]
for i in a:
    if i<minim:
        minim=i 
print (maxm-minim)