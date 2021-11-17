#input
#4
#2 4 5 9  -->A person
#4
#2 4 11 12--->B person
#output--->5 9 11 12
#The rule of the game is, while a person A attacks the other one B,
#  the result of that round is the --distinct powers -- of fire-balls 
# which exist in A but not in B.


n=int(input())
arr1=list(map(int,input().split()))
m=int(input())
arr2=list(map(int,input().split()))
res=[]
for i in arr1:
    if i not in arr2:
        res.append(i)
for j in arr2:
    if j not in arr1:
        res.append(j)
res.sort
#print(res)
for i in res:
    print(i)
