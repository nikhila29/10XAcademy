n=int(input())
list=[]
for i in range(n):
    list.append(int(input()))
new_list=[]
for i in list:
    squ=i*i 
    new_list.append(squ)
new_list.sort()
for i in new_list:
    print(i)
