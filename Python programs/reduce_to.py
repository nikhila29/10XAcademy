n=int(input())
list=[]
for i in range(n):
    list.append(int(input()))

for i in list:
    if max(i)==0:
        print(-1)
    else:
        print(max(i))   
