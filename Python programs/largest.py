def largestElement(A):
    maxm=A[0]
    for i in A:
        if i>maxm:
            maxm=i 
    return maxm


n = int(input())
A = [int(x) for x in input().split()]
print(largestElement(A))