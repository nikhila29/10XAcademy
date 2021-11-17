n,m=map(int,input().split()) #n-row, m-column

matrix = []
for i in range(n):
    a=list(map(int,input().split()))
    matrix.append(a)
sum=0
for n in matrix:
    for j in n:
        if j%2==1:
            sum+=j
print(sum)


