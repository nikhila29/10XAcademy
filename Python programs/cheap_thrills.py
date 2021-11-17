for _ in range(int(input())):#2
    n=int(input())            #3
    arr=list(map(int,input().split()))#3 2 1
    final=sorted(arr) #1 2 3
    set1=set()
    set2=set()
    for j in range(0,n,2):
        set1.add(arr[j]) #3,1
        set2.add(final[j]) #1,3
    print(len(set1-set2)) #1-1=0



