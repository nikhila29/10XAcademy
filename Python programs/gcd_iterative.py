def gcd(a,b):
    if a%b==0:
        return b 
    
    while a%b!=0:
        a,b=b,a%b 
    return b 
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    print(gcd(a,b))