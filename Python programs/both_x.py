def bothCountX(string1, string2, x):
    # Complete this function, and return the list of resultant characters in sorted order
    string1=string1.lower()
    string2=string2.lower()
    dict1={}
    dict2={}
    for i in string1:
    	if i in dict1:
    		dict1[i]+=1
    	else:
    		dict1[i]=1
    for i in string2:
    	if i in dict2:
    		dict2[i]+=1
    	else:
    		dict2[i]=1
    result=[]
    for i in sorted(dict1.keys()):
    	if i in dict2:
    		if dict1[i]==x and dict2[i]==x:
    			result.append(i)
    return(result)

for _ in range(int(input())):
    string1, string2, x = input().split()
    x = int(x)
    print(*bothCountX(string1, string2, x))
    # True False->'0'
