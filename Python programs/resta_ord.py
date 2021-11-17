n=int(input())
t=int(input())
table=[]
cost=[]
list=[]
for i in range(n):
    nums=int(input())
    table.append(nums)
for i in range(n):
    cost.append(int(input()))
bill=[0]*(t+1)
for i in range(n):
    bill[table[i]]+=cost[i]
maxm=-9999
for i in bill:
    if i>maxm:
        maxm=i
for t in range(t+1):
    if bill[t]==maxm:
        print(t)


