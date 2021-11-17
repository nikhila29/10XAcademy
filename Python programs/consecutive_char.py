s=input()
count=1
power=1
for i in range(1,len(s)):
	if s[i]==s[i-1]:
		count+=1
	else:
		power=max(power,count)
		count=1

print(power)