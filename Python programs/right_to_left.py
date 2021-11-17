# name your function as right_to_left_diagonal
def right_to_left_diagonal(m):
	res=[]
	size=len(m)
	for i in range(size):
		for j in range(size):
			if i+j==size-1:
				res.append(m[i][j])
	return res



# Do not change anything below this line
if __name__ == "__main__":
    m = int(input())
    lst = []    
    for val in range(0, m):
        lst.append([int(i) for i in input().split(' ')])
    out = right_to_left_diagonal(lst)
    [print(val) for val in out]