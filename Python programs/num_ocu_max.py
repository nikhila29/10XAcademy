n=int(input())
list=[]
res=[]
for i in range(n):
    list.append(int(input()))

count=1
for i in list:
    if list.count(list[i])==4:
        res.append(list[i])
        break
if len(res)==0:
    print(-1)
else:
    print(res[0])
        
    