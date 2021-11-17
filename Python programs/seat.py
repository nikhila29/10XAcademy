n=int(input())
while n>0:
    c,b=map(int,input().split())

    if b>c:
        print('Invalid')
    elif b%8==1 or b%8==4:
        print('L')
    elif b%8==2 or b%8==5:
        print('M')
    elif b%8==3 or b%8==6:
        print('U')
    elif b%8==7:
        print('SL')
    else:
        print('SU')
    n=n-1
