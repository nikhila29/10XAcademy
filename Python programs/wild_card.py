def wildCard(n,s,i):
    if i==len(n):
        print("".join(s))
        return
    if s[i]=='?':
        s[i]='0'
        wildCard(n,s,i+1)
        s[i]='1'
        wildCard(n,s,i+1)
        s[i]='?'
    else:
        wildCard(n,s,i+1)
n=(input())
s=list(n)
wildCard(n,s,0)