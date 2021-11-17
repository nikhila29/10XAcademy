def bestScore(A,B,C):
    n=len(A)
    A.sort()
    B.sort()
    C.sort()
    i,j,k=0,0,0
    diff=float('inf')
    while i<n and j<n and k<n:
        Tmin=min(A[i],B[j],C[k])
        Tmax=max(A[i],B[j],C[k])
        diff =min(diff,Tmax-Tmin)
        if Tmin==A[i]:
            i+=1
        elif Tmin==B[j]:
            j+=1
        else:
            k+=1
    print(diff)
#DO not edit anything below this line

# Driver code 
A= [int(x) for x in input().split()] 
B= [int(x) for x in input().split()]  
C= [int(x) for x in input().split()]  
bestScore(A,B,C)