N, K = map(int, input().split()) #N=5, k=3
arr = list(map(int, input().split())) #5 4 7 8 1
minn = []
arr.sort() #1 4 5 7 8
for i in range((N-K)+1): #3
    a = abs(arr[i] - arr[(i + K) - 1])
    minn.append(a)
print(min(minn))