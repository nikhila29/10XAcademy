def function(n):
    if n%2==0:
        fun=(n//2)
    else:
        fun=-((n+1)//2)
    return fun
n=int(input())
print(function(n))