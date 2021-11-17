#def pascal(n):
#    pascal=str(11**(n-1))
#    for i in pascal:
#       print(i)
#n=int(input())
#pascal(n)
def get_next_pascal(arr):
    temp=[1]
    for val in range(1,len(arr)):
        temp.append(arr[val-1]+arr[val])
    temp.append(1)
    return temp
def get_pascal(depth):
    if depth==1:
        return [1]
    p=[1,1]
    for i in range(2,depth):
        p=get_next_pascal(p)
    return p
n=int(input())
pascal=get_pascal(n)
[print(i) for i in pascal]