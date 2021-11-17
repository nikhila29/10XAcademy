from collections import Counter
n=int(input())
for _ in range(n):
    str=input()
    myDict =Counter(str)
    count=0
    '''for i in str:
    	if i in myDict:
    		myDict[i]+=1
    	else:
    		myDict[i]=1'''
    if ('r' and 'u' and 'b' and 'y') in myDict:
        count = min(myDict['r'], myDict['u'], myDict['b'], myDict['y'])
    print(count)



    
    #currItem = input()
  #  if currItem in mydict:
   #     mydict[currItem] = mydict[currItem] + 1
   # else:
    #    mydict[currItem] = 1

# how to loop dictionary
#for (key, value) in mydict.items():
    #print(key + " --- " + str(value))




