def comp(val):
    return val[0]+val[1]
for i in range(int(input())):
    n=int(input())
    A=[]
    temp=0
    for j in range(n):
        h,a=map(int,input().split())
        A.append((h,a))
        temp+=a
    A.sort(reverse=True,key=comp)
    print(A[0][0]+A[0][1]+A[1][0]+A[1][1]-temp)