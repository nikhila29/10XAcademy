t=int(input())
for _ in range(t):
    msg_rx=input().split()
    msg_guess=input().split()
#jogod #! siara--#
#raja is good!
    str1="".join(msg_rx)
    str2="".join(msg_guess)
    s1=''
    s2=''
    for i in str1:
        if ord(i)>=65 and ord(i)<=90:
            i=chr(ord(i)+32)
        s1+=i
    for i in str2:
        if ord(i)>=65 and ord(i)<=90:
            i=chr(ord(i)+32)
        s2+=i
    s1=sorted(s1)
    s2=sorted(s2)
    flag=True
    countsDict_1 = {}
    for i in s1:
        if i in countsDict_1:
            countsDict_1[i]+=1
        else:
            countsDict_1[i]=1
    countsDict_2={}
    for j in s2:
        if j in countsDict_2:
            countsDict_2[j]+=1
        else:
            countsDict_2[j]=1
    for i in countsDict_2:
        if i not in countsDict_1 :
            flag=False
if flag==True:
    print("YES")
else:
    print("NO")