def reverseSelectionSort(A, n):
    arr.sort(reverse=True)
    return arr
    

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        print(*reverseSelectionSort(arr, n))