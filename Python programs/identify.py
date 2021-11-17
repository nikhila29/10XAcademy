s=input().lower()
count=0
for i in s:
	ascii=ord(i)
	if ascii<97 or ascii>122:
		count+=1
print(count)