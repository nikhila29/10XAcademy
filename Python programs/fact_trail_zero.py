def trailingZeroes(n):
    # WRITE YOUR CODE HERE
    count=0
    num=n//5
    while num>0:
        count=count+int(num)
        num=num*5
    return int(count)
 
# DO NOT CHANGE ANYTHING BELOW THIS LINE
num_tests=int(input())
for _ in range(num_tests):
    n=int(input())
    print(trailingZeroes(n))