import math
def stamps(arr):
    return math.ceil(len(arr)/2)
n=int(input())
arr=list(map(int,input().split()))
#Both of us will have N/2 stamps each. Thus N is even--->n=6--6/2=3
#stamps=n//2
print(stamps(arr))
#1 1 2 2 3 3
dict={} #{1:2,2:2,3:2},count variables--types of stamps

