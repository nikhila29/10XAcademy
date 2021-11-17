def calSumUtil( A , B , n , m ): 
   # Implement this 
   # A is the first array
   # n is size of array A
   # B is the second array
   # m is size of array B
   num1=int("".join(map(str,A)))
   num2=int("".join(map(str,B)))
   res=num1+num2
   res=[int(x) for x in str(res)]
   return res
  
# Wrapper Function 
def calSum(a, b, n, m ): 
  
    # Making first array which have 
    # greater number of element
    # A is the first array
    # n is size of array A
    # B is the second array
    # m is size of array B 
    if n >= m: 
        return calSumUtil(a, b, n, m) 
    else: 
        return calSumUtil(b, a, m, n) 
  
# Driven Code 
testCase = int(input())
for _ in range(testCase):
	A = list(map(int,input().split()))
	B = list(map(int,input().split()))
	res = calSum(A, B, len(A), len(B))
	print(*res)