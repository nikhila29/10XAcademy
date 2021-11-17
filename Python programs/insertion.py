def insert(arr,n):
    arr.sort()
    return arr

### DO NOT EDIT ANYTHING BELOW THIS LINE

if __name__=='__main__':
    n = int(input())
    arr = [int(x) for x in input().split()]
    insert(arr, n)
    print(*arr)