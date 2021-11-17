n,k=map(int,input().split()) #n---crackers, k---users
div=(n+k)/2
if div%2==0:
    print(0)
else:
    print(1)