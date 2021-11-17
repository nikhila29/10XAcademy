def selectionSort(A, n):
    for start in range(len(A)):
        i=start
        ind_min=start
        for i in range(start,len(A)):
            if (A[i]<A[ind_min]):
                ind_min=i 
        A[start],A[ind_min]=A[ind_min],A[start]
    return (A)
    
if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        print(*selectionSort(arr, n))