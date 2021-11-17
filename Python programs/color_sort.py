'''n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
new_arr=[]
while arr:
    minim=arr[0]
    for i in arr:
        if i<minim:
            minim=i
    new_arr.append(i)
    arr.remove(minim)
for x in new_arr:
    print(x)
'''
n=int(input())
zero=0
one=0
two=0
#while (boolean expression -> true/false)
for _ in range(n):
    temp=int(input())
    if temp==0:
        zero+=1
    elif temp==1:
        one+=1
    else:
        two+=1
while zero:
    print(0)
    zero-=1
while one:
    print(1)
    one-=1
while two:
    print(2)
    two-=1


