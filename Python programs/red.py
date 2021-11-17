s=input()
r=0
g=0
for i in s:
    if i=='R':
        r+=1
    else:
        g+=1
print(min(r,g))
