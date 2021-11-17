n=int(input())
arr=list(map(int,input().split()))
one=0
two=0
three=0
four=0
five=0
#while (boolean expression -> true/false)
for i in arr:
    temp=i 
    if temp==1:
        one+=1
    elif temp==2:
        two+=1
    elif temp==3:
        three+=1
    elif temp==4:
        four+=1
    else:
        five+=1
while one:
    print(1)
    one-=1
while two:
    print(2)
    two-=1
while three:
    print(3)
    three-=1
while four:
    print(4)
    four-=1
while five:
    print(5)
    five-=1