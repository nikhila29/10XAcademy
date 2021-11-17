def parenthesis_util(result,sequence,no,nc,n):
	if nc==n:
		result.append(sequence)
		return
	if nc<no:
		parenthesis_util(result,sequence+")",no,nc+1,n)
	if no<n:
		parenthesis_util(result,sequence+"(",no+1,nc,n)
def getAllBalancedParan(n):
	result=[]
	sequence=""
	parenthesis_util(result,sequence,0,0,n)
	return (result)
	

# Do not edit anything below
n = int(input())
allBalancedParan = getAllBalancedParan(n)
allBalancedParan.sort()
for expr in allBalancedParan:
    print(expr)