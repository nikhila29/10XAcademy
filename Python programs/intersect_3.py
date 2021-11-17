def intersect(arr1,arr2,arr3):
    p1=0
    p2=0
    p3=0
    result=[]
    while p1<len(arr1) and p2<len(arr2) and p3<len(arr3):
        if arr1[p1]==arr2[p2] and arr1[p1]==arr3[p3]:
            result.append(arr1[p1])
            p1+=1
            p2+=1
            p3+=1
        elif arr1[p1]>arr2[p2]:
            p2+=1
        elif arr1[p1]<arr2[p2]:
            p1+=1
        elif arr2[p2]>arr3[p3]:
            p3+=1
        elif arr2[p2]<arr3[p3]:
            p2+=1
        elif arr3[p3]>arr1[p1]:
            p1+=1
        else:
            p3+=1
    if len(result)==0:
        result.append(-1)
    return result
n1=int(input())
arr1=[]
for _ in range(n1):
    arr1.append(int(input()))
n2=int(input())
arr2=[]
for _ in range(n2):
    arr2.append(int(input()))
n3=int(input())
arr3=[]
for _ in range(n3):
    arr3.append(int(input()))
for element in intersect(arr1, arr2,arr3):
        print(element)