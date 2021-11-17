def solve(n,dials,max_limit):
    for i in range(n):
        j=int(input())
        dials[j-1]+=1
        if dials[j-1]==max_limit:
            return(j)
    return 0
n=int(input())
dials=[0]*n
max_limit=int(input())
n=int(input())
print(solve(n,dials,max_limit))            