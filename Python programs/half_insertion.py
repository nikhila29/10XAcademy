string=input()
n=len(string)//2
str1=string[:n]
str2=string[n:]
sorted_str2= "".join(sorted(str2))
print(str1+sorted_str2)