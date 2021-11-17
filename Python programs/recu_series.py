def recursiveSeries(i):
    if i<=9:
        return i
    if i%2==0:
        return recursiveSeries(i-9)
    else:
        return recursiveSeries(i-10)
for _ in range(int(input())):
    n=int(input())
    print(recursiveSeries(n))

