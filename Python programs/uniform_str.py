# your code goes here
n = int(input())
s = input()
dict1 = {}
for i in s:
	if i in dict1:
		dict1[i] += 1
	else:
		dict1[i] = 1
value1 = -1
value2 = -1
count1 = 0
count2 = 0
flag = 0
for value in dict1.values():
	if(value1 == -1):
		value1 = value
		count1 += 1
	elif (value1 == value):
		count1 +=1
	elif(value2 == -1):
		value2 = value
		count2 += 1
	elif(value2 == value):
		count2 += 1
	else:
		flag = 1
		break
	if((count1>1) and (count2>1)):
		flag = 1
		break
if(flag == 0):
	print('True')
else:
	print('False')
