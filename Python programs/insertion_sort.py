def insertionSort(A, n):
    for key_idx in range(n):
        key=A[key_idx]
        j=key_idx-1
        while j>=0 and key< A[j]:
            A[j+1]=A[j]
            j-=1
        A[j+1]=key
    return (A)
if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        print(*insertionSort(arr, n))