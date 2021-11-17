n=int(input())
l=map(int,input().split())
count=0
for i in l:
    if i<0:
        count+=1
        
        
print(count) 