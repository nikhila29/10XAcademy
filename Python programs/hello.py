givenNumbers=[]
n=int(input())
for i in range(0,n):
    num=int(input())
    givenNumbers.append(num)
sortedlist=[]
for swappingIndex in range(n):
    minIndex=swappingIndex
    for remaininglistIndex in range(swappingIndex,n):
        if (givenNumbers[remaininglistIndex]<givenNumbers[minIndex]):
            minIndex=remaininglistIndex
    tempValue=givenNumbers[swappingIndex]
    givenNumbers[swappingIndex]=givenNumbers[minIndex]
    givenNumbers[minIndex]=tempValue
for x in givenNumbers:
    print(x)
