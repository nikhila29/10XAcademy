n=int(input())
for _ in range(n):
    s,t=input().split()
    str1=sorted(s)
    str2=sorted(t)
    if str1==str2:
        print(True)
    else:
        print(False)

