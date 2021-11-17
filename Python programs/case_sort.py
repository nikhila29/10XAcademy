def casesort(ssr,n):
    lowerstr=[]
    upperstr=[]
    for i in range(n):
        if (ssr[i]>='a' and ssr[i]<='z'):
            lowerstr.append(ssr[i])
        if (ssr[i]>='A' and ssr[i]<='Z'):
            upperstr.append(ssr[i])
    upperstr.sort()
    lowerstr.sort()
    i,j=0,0
    for k in range(n):
        if ssr[k]>='a' and ssr[k]<='z':
            ssr[k]=lowerstr[i]
            i+=1
        elif ssr[k]>='A' and ssr[k]<='Z':
            ssr[k]=upperstr[j]
            j+=1
    return ''.join(ssr)
nolet=int(input())
s=str(input())
casestr=[i for i in s]
print(casesort(casestr,nolet))