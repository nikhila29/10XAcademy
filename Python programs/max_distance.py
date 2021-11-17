n=int(input())
arr=list(map(int,input().split()))
maxim=-999999999999
minim=999999999999
for i in range(len(arr)):
    maxim=max(maxim,(i-1)*arr[i])
    minim=min(minim,(i+1)*arr[i])
print(maxim-minim)