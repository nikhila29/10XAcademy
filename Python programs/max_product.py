'''n=int(input())
list=[]
for i in range(n):
    list.append(int(input()))
for i in range(len(list)-1):
    product=list[i]*list[i+1]
maxm=1
if product>maxm:
    maxm=product
    print(maxm)'''
n=int(input())
list=[]
for i in range(n):
    list.append(int(input()))
result=[i*j for i,j in zip(list[:-1],list[1:])]
print(max(result))
