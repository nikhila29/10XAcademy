'''n,q=map(int,input().split())
time=list(map(int,input().split()))
score=list(map(int,input().split()))
time.sort(reverse=True)
cumulative_time=[time[0]]
for i in range(1,n):
    cumulative_time.append(cumulative_time[i-1]+time[i])
for i in range(q):
    x=int(input())
    print(cumulative_time[x-1])'''
n,q=map(int,input().split())
time=list(map(int,input().split()))
score=list(map(int,input().split()))
score.sort(reverse=True)
time.sort(reverse=True)
maxim=max(time,score)
cumulative_time=[time[0]]
for i in range(1,n):
    cumulative_time.append(cumulative_time[i-1]+time[i])
for i in range(q):
    x=int(input())
    print(cumulative_time[x-1])


    
