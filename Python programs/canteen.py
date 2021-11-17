'''n,k=map(int,input().split())
arr=list(map(int,input().split()))
b_charged=int(input())
sum=0
for i in arr:
    sum+=i
    b_actual=(sum-arr[k])//2
if b_charged>b_actual:
    print(b_charged-b_actual)
else:
    print("It is Correct!")'''
# your code goes here
# input

n, k = map(int, input().split())

bills = list(map(int,input().split()))

b = int(input())

# s = 0
# for i in range(n):
# 	if i!=k:
# 		s += bills[i]

b_actual = (sum(bills) - bills[k])//2

if b==b_actual:
	print("It is Correct!")
else:
	print(b-b_actual)

