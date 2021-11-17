def reverse(arr):
        if len(arr)==0:
            return arr
        return reverse(arr[1:])+ arr[0]
n=int(input())
for _ in range(n):
    arr=str(input())
    print(reverse(arr))