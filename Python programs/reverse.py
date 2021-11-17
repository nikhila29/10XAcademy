n=int(input())
if(n<0):
    n=n*-1
    rev=int(str(n)[::-1])
    print(-1*rev)
else:
    rev=int(str(n)[::-1])
    print(rev)