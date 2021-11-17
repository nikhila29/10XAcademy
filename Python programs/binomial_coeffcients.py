def binomialCoeff(n, r):
    if n==r:
        return 1
    if r==0:
        return 1
    if r==1:
        return n
    return (binomialCoeff(n-1,r-1) + binomialCoeff(n-1,r))


# Do not edit anything below
if __name__ == "__main__":
    numTcs = int(input())
    for index in range(numTcs):
        inputInts = input().split(' ')
        n = int(inputInts[0])
        r = int(inputInts[1])
        print(binomialCoeff(n, r))