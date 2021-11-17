def sumOfFirstN(n):
    if n==1:
        print(1,1)
        return 1
    result = n + sumOfFirstN(n-1)
    print(n,result)
    return(result)

# Do not edit anything below
if __name__ == "__main__":
    n = int(input())
    sumOfFirstN(n)