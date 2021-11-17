def recur(n):
    if n==1:
        return 1
    
    fn=1
    start=(n*(n-1))//2+1
    for i in range(start,start+n):
        fn*=i
    return recur(n-1)+fn

for i in range(int(input())):
    print(recur(int(input())))