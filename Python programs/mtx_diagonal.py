# name your function as change_diagonal and it should take list as input
def change_diagonal(arr):
	n=len(arr)
	for i in range(n):
		for j in range(n):
			if i==j:
				if arr[i][j]>=0:
					arr[i][j]=1
				else:
					arr[i][j]=0
	return arr



# Do not change anything below this line.
if __name__ == "__main__":
    val = int(input())
    lst = []
    for index in range(0, val):
        lst.append([int(i) for i in input().split(' ')])
    out = change_diagonal(lst)
    for lst1 in out:
        print(" ".join(str(i) for i in lst1))