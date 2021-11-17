#output[i] is equal to the product of all the elements of nums except nums[i].
#                  0 1 2 3
#24 12 8 6--output,1 2 3 4--input
#24=2*3*4 except 1--->0--2 3 4
#12=1*3*4 except 2--->1--1 3 4
#8=1*2*4 except  3--->2--1 2 4
#6=1*2*3 except  4--->3--1 2 3
n=int(input())
for _ in range(n):
    t=int(input())
    arr=list(map(int,input().split()))
    arr1=[]
    if len(arr)==1:
        print(1)
    if len(arr)==0:
        print(0)
    if len(arr)>1:
        p=1
        '''for i in arr:
            p=(p*i)
        for i in range(t):
            d=p//arr[i]
            arr1.append(d)
        print(*arr1)'''
        for i in arr:
            arr.remove(i)
            p*=i
            print(p)



