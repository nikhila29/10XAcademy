rows,cols = map(int,input().split())
lst1 = []
lst2=[]
for val in range(0, rows):
    lst1.append([int(i) for i in input().split(' ')])
l,r,t,b=map(int,input().split())
rows=len(lst1[0])
cols=len(lst1)
for i in range(t-1,b):
    lst2.append(lst1[i][l-1:r])
for i in range(len(lst2)):
    print(*lst2[i])