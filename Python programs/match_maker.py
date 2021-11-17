def matchMaker(girls,boys,n):
    girls.sort()
    boys.sort(reverse=True)
    res=0
    for i in range(n):
        if girls[i]%boys[i]==0 or boys[i]%girls[i]==0:
            res+=1
    return res
for i in range(int(input())):
    n=int(input())
    girls=[int(i) for i in input().split()]
    boys=[int(i) for i in input().split()]
    print(matchMaker(girls,boys,n))