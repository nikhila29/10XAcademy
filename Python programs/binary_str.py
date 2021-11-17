n=int(input())
res=[]
def binaryStr(k,s):
    if k==0:
        res.append(s)
        return
    
    if s=="":
        binaryStr(k-1,s+'0')
        binaryStr(k-1,s+'1')
    elif s[len(s)-1]=='1':
        binaryStr(k-1,s+'0')
    else:
        binaryStr(k-1,s+'0')
        binaryStr(k-1,s+'1')
binaryStr(n, "")
res.sort()
print(*res)