# your code goes here
t = int(input())
for test in range(t):
	s = input()
	dict1 = {}
	for i in s:
		if i in dict1:
			dict1[i] += 1
		else:
			dict1[i] = 1
	index = -1
	for i in range(0,len(s)):
		if dict1[s[i]] == 1:
			index = i
			break
	print(index)
