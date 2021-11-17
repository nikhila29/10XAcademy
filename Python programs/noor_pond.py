t=int(input())
for _ in range(t):
    n=int(input())
    E=[]
    S=[]
    for i in range(n):
        s,e=[int(i) for i in input().split()]
        S.append(s)
        E.append(e)
    S.sort()
    E.sort()
    s=n-1
    e=n-1
    maxm=1
    count=0
    while s>=0 and e>=0:
        if S[s]<=E[e]:
            count-=1
            e-=1
        else:
            count+=1
            s-=1
        maxm=max(maxm,count)
    print(maxm)