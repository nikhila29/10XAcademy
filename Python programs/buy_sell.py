n=int(input())  # no. of days of data
prices=[]       #price of each day
for _ in range(n):
    prices.append(int(input()))
profit=0
next_max=prices[0]
for i in range(len(prices)-1):
    if next_max==prices[i]:
        next_max=max(prices[i+1:])
    temp=next_max-prices[i]
    if temp>profit:
        profit=temp
print(profit)
