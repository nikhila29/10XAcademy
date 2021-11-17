n=int(input())
arr=[]
for i in range(n):
    n,s,m=input().split() #name,scholar,marks
    s,m=int(s),int(m)
    arr.append([n,s,m])
arr=sorted(arr,key=lambda x:x[1])  # scholar
arr=sorted(arr,key=lambda x:x[0])  #name
arr=sorted(arr,key=lambda x:x[2],reverse=True) # marks
for i in arr:
    print(*i)
